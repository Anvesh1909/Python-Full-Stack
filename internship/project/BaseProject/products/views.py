from django.shortcuts import render
from products.models import Products


def showProducts(request):
    context = {
        'products' : Products.objects.all(),
        'publishedProjects' : Products.objects.filter(is_published=True)
    }
    return render(request,'showProducts.html',context)