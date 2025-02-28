from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=30,unique=True,null=False)
    password = models.CharField(max_length=234)
    mobileNo = models.CharField(max_length=20)
