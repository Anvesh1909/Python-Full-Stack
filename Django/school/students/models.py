from django.db import models

# Create your models here.


class Students(models.Model):
    rollNo = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=200)
    standard = models.IntegerField()
    presentage = models.FloatField()


    def __str__(self):
        return self.name


