from django.shortcuts import render
from students.models import Students
# Create your views here.
def indexView(request):
    context = {
        "students" : Students.objects.all()
    }
    return render(request,'index.html',context)