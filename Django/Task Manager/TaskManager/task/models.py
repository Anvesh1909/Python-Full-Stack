
from django.db import models

from django.contrib.auth.models import User

class Tasks(models.Model):

    STATUS_CHOICES = [
        ('TO DO', 'TO DO'),
        ('IN PROCESS', 'In Process'),
        ('DONE', 'Done'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now=True)
