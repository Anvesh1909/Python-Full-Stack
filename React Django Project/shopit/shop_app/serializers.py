from rest_framework import serializers

from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class DetailsProductSerializer(serializers.ModelSerializer):
    similar_products = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id","name","price","slug","image","description","similar_products"]
    
    def get_similar_products(self,product):
        products = Product.objects.filter(category = product.category).exclude(id=product.id)
        serializer = ProductSerializers(products,many=True)
        return serializer.data
    
