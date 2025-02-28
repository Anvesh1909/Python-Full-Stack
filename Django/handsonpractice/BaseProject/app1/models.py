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







# many to one or one to many relations

class Reporter(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=21)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username

class Artical(models.Model):
    headlines = models.CharField(max_length=255)
    pubishDate = models.DateField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)  

    def __str__(self):
        return self.headlines
  