from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200)
    present = models.BooleanField()
    phoneNo = models.IntegerField()