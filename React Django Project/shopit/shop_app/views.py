from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop_app.serializers import ProductSerializers
from shop_app.models import Product
# Create your views here.

@api_view(["GET"])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products,many = True)

    return Response(serializer.data)