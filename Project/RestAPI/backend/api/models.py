from django.db import models

# Create your models here.
class StudentTable(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    