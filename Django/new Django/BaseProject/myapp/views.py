from django.shortcuts import render

# Create your views here.
def index(request):
    # context is sending information from backend to frontend
    # context is dictionary type which store in the form of key and value pair

    Students = [
        {"id":1,"name":"Anvesh","age":22},
        {"id":2,"name":"Prerana","age":23},
        {"id":3,"name":"Pooja","age":23},
    ]

    context = {
        'name' : 'prerana',
        'age' : 23,
        'course' : 'python full stack',

        'students' : Students
    }
    return render(request,'index.html',context) 

from myapp.models import Student

def students(request):
    context = {
        'students' : Student.objects.all()
    }
    return render(request,'students.html',context)