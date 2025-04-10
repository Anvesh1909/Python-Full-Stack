from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    phoneNo = models.CharField(max_length=15)
    bio = models.TextField()