from django.shortcuts import render,redirect
from crudForms.models import Students
from crudForms.forms import StudentForm

# Create your views here.
def readAll(request):

    if request.method == "POST":
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()

    context = {
        'students' : Students.objects.all(),
        'studentForm' : StudentForm()
    }

    return render(request,'crudReadAll.html',context)


def updateStudent(request,id):
    student = Students.objects.get(id=id)

    if request.method == "POST":
        student = StudentForm(request.POST,instance=student)

        if student.is_valid():
            student.save()

        return redirect('formReadAll')
    

    context = {
        "studentForm" : StudentForm(instance=student)
    }

    return render(request,"crudUpdate.html",context)



def deleteStudent(request,id):
    stu = Students.objects.get(id=id)
    stu.delete()
    return redirect("formReadAll")