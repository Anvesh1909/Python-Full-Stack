from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize

from shop_app.serializers import DetailsProductSerializer, ProductSerializers
from shop_app.models import Product
# Create your views here.

@api_view(["GET"])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products,many=True)

    # print(serializer.data) 
    
    return Response(serializer.data)


@api_view(['GET'])
def product_details(request,slug):
    product = Product.objects.get(slug=slug)
    serializer = DetailsProductSerializer(product)
    return Response(serializer.data)