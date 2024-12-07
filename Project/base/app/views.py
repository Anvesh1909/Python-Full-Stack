from django.shortcuts import render

from .models import employees
# Create your views here.


def index(request):
    context = {
        'emp' : employees.objects.all()
    }
    return render(request,"index.html",context)