from django.db import models

class basics(models.Model):

    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, default='NA')
    