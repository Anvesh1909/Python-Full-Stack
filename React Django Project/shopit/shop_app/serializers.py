from itertools import product
from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.Serializer):
    class Meta:
        model = Product
        fields = ["id",'name','slug','image','description','category','price']
        