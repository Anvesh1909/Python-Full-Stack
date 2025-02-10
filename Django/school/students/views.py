from django.shortcuts import render

# Create your views here.
from django.views import View
from students.models import Students

class IndexView(View):
    def get(self,request):
        # allStudents = Students.objects.all()  # ORM (Object retational mapping)
        # print(allStudents)
        student = Students.objects.get(rollNo = 4)
        allStudents = Students.objects.all()

        context =  {
            "student" : student,
            "allStu" : allStudents
        }
        return render(request,'index.html',context)
    

# print("HELLO")
# from students.models import Students

# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
# Students.objects.create(rollNo="3",name="bunny",standard=5,presentage=505)
