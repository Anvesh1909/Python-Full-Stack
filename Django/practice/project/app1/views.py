from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    context = {
        "name" : "Anvesh",
        "course" : "Python",
        "age" : 22
    }
    
    return render(request,"home.html",context)

# def about(request):
#     return HttpResponse("About page")

# def service(request):
#     return HttpResponse("service page")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"services.html")

