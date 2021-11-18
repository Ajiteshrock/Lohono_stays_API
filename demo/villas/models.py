from django.db import models
from django.contrib.auth.models import User

class Villa(models.Model):
    name      = models.CharField(max_length=59)
    price     = models.FloatField()
    check_in  = models.DateTimeField()
    check_out = models.DateTimeField()
    def __str__(self):
        return self.name

    



