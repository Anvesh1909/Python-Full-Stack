from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name

