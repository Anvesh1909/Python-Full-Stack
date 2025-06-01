from django.db import models

# Create your models here.
class Tasks(models.Model):

    status_choices = {
        "Not started" : "Not Started",
        "Pending" : "Pending",
        "Done" : "Done"
    }

    name = models.CharField(max_length=50)
    status = models.CharField(choices=status_choices , max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
