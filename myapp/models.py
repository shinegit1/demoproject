from django.db import models


# Create your models here.
class Contact:
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
