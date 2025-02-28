from django.shortcuts import render

# Create your views here.
from ORM.models import Employee
from django.http import HttpResponse

def addRecords(request):
    obj = Employee.objects.create(name="jessica",mobile="123456543",email="jessica@gmail.com")
    return HttpResponse(obj)

