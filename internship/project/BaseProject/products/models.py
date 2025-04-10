from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=99)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=20,decimal_places=2)
    discription = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)