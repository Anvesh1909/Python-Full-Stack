from turtle import mode
from attr import field
from rest_framework import serializers

from . models import Category,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'