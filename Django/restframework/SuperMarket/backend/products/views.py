from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize

from products.serializers import ProductSerializer

from . models import Product

from rest_framework import status

@api_view(['GET','POST'])
def productsView(request):
    if request.method == "GET":
        
        id = request.query_params.get('id')
        if id:
            try:
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product)
            except Exception as e:
                return Response("Object not found",status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data)
        else:
            return Response("Enter correct fields",status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def categoryView(request):
    if request.method == "GET":    
        id = request.query_params.get('id')
        if id:
            try:
                product = Product.objects.filter(category=id)
                serializer = ProductSerializer(product,many=True)
            except Exception as e:
                return Response("Object not found",status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)