from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=20, null=True)


