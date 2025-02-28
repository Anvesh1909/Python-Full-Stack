from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def httpResponseView(request):
    return HttpResponse("This is functional view httpResponse")



# to create class view
from django.views import View

class HttpClassView(View):
    def get(self,request):
        return HttpResponse("This is class view")




# to create a render function
def homeView(request):
    # in render we can pass 3 arguments
    return render(request,"home.html")



from app1.models import Students

class AllStudents(View):
    def get(self,request):
        # allStudents = Students.objects.all()  # ORM (Object retational mapping)
        # print(allStudents)
        student = Students.objects.get(rollNo = 4)
        allStudents = Students.objects.all()

        context =  {
            "student" : student,
            "allStu" : allStudents
        }
        return render(request,'allStudents.html',context)
    


from app1.forms import StudentsForm

def studentView(request):
    data = StudentsForm()
    return render(request,"studentform.html",{'data' : data})




from app1.forms import EmployeeRegistration

def employeeRegistrationView(request):
    data = EmployeeRegistration()
    return render(request,"employee.html",{"data":data})





from app1.models import Employees

def getEmployee(request):
    # obj = Employees.objects.get(id = 12)
    try:
        obj = Employees.objects.get(id = 1)
        # obj = Employees.objects.all()
    except:
        obj = "id not found"
    finally:
        return HttpResponse(obj)
    


def setCookie(request):
    responce = render(request,"setCookie.html")
    responce.set_cookie("name","Anvesh")
    return responce


def getCookie(request):
    name = request.COOKIES.get("name","cookie not found")
    return render(request,"getCookie.html",{"name":name})

def deleteCookie(request):
    responce = render(request,"deleteCookie.html")
    responce.delete_cookie("name")
    return responce
                 




# many to one or one to many relations