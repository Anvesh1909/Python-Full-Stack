from django.db import models

# Create your models here.


class Students(models.Model):
    rollNo = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=200)
    standard = models.IntegerField()
    presentage = models.FloatField()


    def __str__(self):
        return self.name




# for exception handling
class Employees(models.Model):
    Ename = models.CharField(max_length=255)
    Esal = models.FloatField()
    role = models.CharField(max_length=100)
    jdate = models.DateField()

