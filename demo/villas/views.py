from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import  VillaSeralizer
from rest_framework.response import Response
from rest_framework import status
from .models import Villa
from rest_framework import generics
from django.db.models import Q
import datetime
import pytz
utc = pytz.UTC
class VillaView(APIView):

    def get(self,request):
        villas = Villa.objects.all()
        serializer =  VillaSeralizer(villas,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def post(self,request):
        data = self.request.data
        data = dict(data)
        check_in = data['check_in']
        check_out = data['check_out']

        query_param = self.request.query_params.get('sort',None)

        villalist = Villa.objects.all().exclude(
                    check_in__lte=data['check_out'],
                    check_out__gte=data['check_in']
                )
        villalist = Villa.objects.filter(Q(check_in__lte=data['check_out']) & Q(check_out__gte=data['check_in']))
        
        if len(villalist)>1:
            avg_price = 0
            for i in villalist:
                avg_price+=i.price
           
            avg_price = avg_price/len(villalist)
            gst = (avg_price) * 0.18 
            avg_price = avg_price + gst
            response_data = {'Villas_available_and_price':[],
                            'Avg_price':avg_price}
            for i in villalist:
                response_data['Villas_available_and_price'].append((i.name,i.price))
        else:
            return Response({"message":"No Villa Available"},status=status.HTTP_202_ACCEPTED)

        if query_param == None:
           return Response(response_data,status=status.HTTP_202_ACCEPTED)
        else:
            def Sort_Tuple(tup): 
                # getting length of list of tuples containng villas and price
                lst = len(tup) 
                for i in range(0, lst): 
                    
                    for j in range(0, lst-i-1): 
                        if (tup[j][1] > tup[j + 1][1]): 
                            temp = tup[j] 
                            tup[j]= tup[j + 1] 
                            tup[j + 1]= temp 
                return tup 
            
            response_data['Villas_available_and_price']=Sort_Tuple(response_data['Villas_available_and_price'])
            return Response(response_data,status=status.HTTP_202_ACCEPTED)
            
               
class Villa_Rate(APIView):

    def post(self,request):
        data = request.data
        check_in = datetime.datetime.strptime(data['check_in'],"%Y-%m-%d %H:%M")
        check_out = datetime.datetime.strptime(data['check_out'],"%Y-%m-%d %H:%M")
        
        stay_days = (check_out-check_in)
        def is_available(check_in,check_out):
            villa_object = Villa.objects.all()
            villas_list = []
            price = []
            for i in villa_object:
                check_in  = check_in.replace(tzinfo=utc)
                check_out = check_out.replace(tzinfo=utc)
                if i.check_in.date() > check_out.date() and i.check_out.date()<=i.check_in.date():
                    villas_list.append(True)
                    price.append(int(i.price))  
                else:
                    villas_list.append(False)
            return (all(villas_list),(sum(price)/len(villas_list)))
            
            
        if is_available(check_in, check_out)[0]:
            rate = is_available(check_in, check_out)[1]
            rate = rate + (rate*0.18)
            return Response({"Availability":"Villas Are Available",
                             "Total Price":rate},status=status.HTTP_202_ACCEPTED)
   
        return Response({'message':"Villas Are Not Available"})
   
   



