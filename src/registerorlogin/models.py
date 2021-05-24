from django.db import models


# Create your models here.
class UserModel(models.Model):
    userid = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)