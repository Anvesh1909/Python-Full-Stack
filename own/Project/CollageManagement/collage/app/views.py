from django.shortcuts import render,redirect

from . forms import * 
from . models import *

# Create your views here.
def index(request):





    # context={

    #     'Department' : Department.objects.all(),
    #     'Teachers' : Teachers.objects.all(),
    #     'TeacherProfile' : TeacherProfile.objects.all(),
    #     'Subject' : Subjects.objects.all(),
    #     'Student' : Students.objects.all(),
    #     'StudentSubjects' : StudentSubjects.objects.all(),
    #     'Library' : Library.objects.all(),



    #     'DepartmentForm' : DepartmentForm,
    #     'TeachersForm' : TeachersForm,
    #     'TeacherProfileForm' : TeacherProfileForm,
    #     'SubjectForm' : SubjectForm,
    #     'StudentForm' : StudentForm,
    #     'StudentSubjectsForm' : StudentSubjectsForm,
    #     'LibraryForm' : LibraryForm
    # }
    return render(request,'index.html')



def DepartmentView(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid:
            form.save()
    
    context = {
        'Department' : Department.objects.all(),
        'DepartmentForm' : DepartmentForm,
    }
    return render(request,'Department.html',context)


def TeachersView(request):
    if request.method == "POST":
        form = TeachersForm(request.POST)
        if form.is_valid:
            form.save()
    context= {
        'Teachers' : Teachers.objects.all(),
        'TeachersForm' : TeachersForm,
    }
    return render(request,"Teachers.html",context)


def TeacherProfileView(request):
    if request.method == "POST":
        form = TeacherProfileForm(request.POST)
        if form.is_valid:
            form.save()

    context = {
        'TeacherProfile' : TeacherProfile.objects.all(),
        'TeacherProfileForm' : TeacherProfileForm,
    }
    return render(request,"TeacherProfile.html",context)




def SubjectView(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid:
            form.save()

    context = {
        'Subject' : Subjects.objects.all(),
        'SubjectForm' : SubjectForm,
    }
    return render(request,"Subjects.html",context)



def StudentView(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()

    context={
        'Student' : Students.objects.all(),
        'StudentForm' : StudentForm,
    }
    return render(request,"Student.html",context)




def StudentSubjectsView(request):
    if request.method == "POST":
        form = StudentSubjectsForm(request.POST)
        if form.is_valid:
            form.save()

    context = {
        'StudentSubjects' : StudentSubjects.objects.all(),
        'StudentSubjectsForm' : StudentSubjectsForm,
    }    

    return render(request,"StudentSubjects.html",context)



def LibraryFormView(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid:
            form.save()

    context = {
        'Library' : Library.objects.all(),
        'LibraryForm' : LibraryForm
    }
    return render(request,"Library.html",context)



