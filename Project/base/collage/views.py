from django.shortcuts import render,redirect

from . models import * 

# Create your views here
def index(request):
    return render(request,'collage.html')



def DepartmentView(request):
    if request.method == "POST":
        name = request.POST.get("DeptName")
        head = request.POST.get("Head")
        Department.objects.create(name= name,head= head)
        
    context = {
        'dept' : Department.objects.all()
    }
    return render(request,'Department.html',context)