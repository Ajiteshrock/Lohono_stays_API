
import os
import django

from faker import Faker
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo.settings')

#running the setup file
django.setup()
from villas.models import Villa
import datetime

date1 = '01-01-2021 12:00'
date2 = '31-12-2021 11:59'
import random
date1 = datetime.datetime.strptime(date1, "%d-%m-%Y %I:%M")
date2 = datetime.datetime.strptime(date2, "%d-%m-%Y %I:%M")
fake_gen = Faker()
for i in range(50):
    name      = fake_gen.name()+" villa"
    check_in  = fake_gen.date_time_between(date1,date2)
    check_out = fake_gen.date_time_between(date1,date2)
    price     = random.randint(30000, 50000)
    object1   = Villa.objects.get_or_create(name=name,check_in=check_in,check_out=check_out,price=price)