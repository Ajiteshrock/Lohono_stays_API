# Lohono_stays_API

# This is demo API of the assignment given 


### Running Code

# pip install requirements.txt
# clone the repo 
# got to >> demo 
# python manage.py runserver


# Endpoints

### api/villas/  (GET)
# This will give the all villas list their price and their booked check_in and check_out 

### api/villas/ (POST)
# This will give all available villas and their prices 
# Also the average price including 18% GST

## Request Format

## {
##   "check_in": "2021-03-06 11:52",
##   "check_out": "2021-07-09 12:42",
   
## }
 
 # Response Format 
 
## { "Villas_available_and_price": [ [ "Jennifer Evans villa",  33698.0 ], "Avg_price": 40741.51219512195   }


### api/villas/?sort="price
## the list which we will be sorted on the bases of Price
