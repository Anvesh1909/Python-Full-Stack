from django.shortcuts import render,redirect
from crud.models import Students

# Create your views here.
def readAll(request):

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")

        Students.objects.create(name=name,age=age,course=course) 

    context = {
        'students' : Students.objects.all()
    }

    return render(request,'readAll.html',context)


def updateStudent(request,id):
    student = Students.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")

        student.name = name
        student.age = age
        student.course = course
        student.save()

        return redirect("readAll")


    context = {
        "student" : student
    }

    return render(request,"update.html",context)



def deleteStudent(request,id):
    stu = Students.objects.get(id=id)
    stu.delete()
    return redirect("readAll")