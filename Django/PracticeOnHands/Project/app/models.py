from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)


