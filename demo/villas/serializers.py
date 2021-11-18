from rest_framework.serializers import ModelSerializer, Serializer
from .models import Villa
from rest_framework import serializers
class VillaSeralizer(ModelSerializer):
    check_in = serializers.DateTimeField()
    check_out = serializers.DateTimeField()  
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Villa
        fields = ('check_in','check_out','name','price')
     
     