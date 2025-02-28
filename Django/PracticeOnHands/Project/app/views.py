from django.shortcuts import render

# Create your views here.

# first time welcome
# secound time welcome back

def homeView(request):

    context = {
        "visit" : request.COOKIES.get("visit",0)
    }

    response = render(request,'welcome.html',context)

    response.set_cookie('visit',1)

    return response



from app.models import Students

def home(request):
    
    if request.method == "GET":
        search = request.GET.get("search",None)
        if search:
            data = Students.objects.filter(name__startswith=search) | Students.objects.filter(branch__startswith=search) 
        else:
            data = Students.objects.all()

        context = {
            "students" : data
        }

    return render(request,'index.html',context)



from app.forms import StudentForm

def studentForm(request):

    if request.method == "GET":
        search = request.GET.get("search",None)
        if search:
            data = Students.objects.filter(name__startswith=search) | Students.objects.filter(branch__startswith=search) 
        else:
            data = Students.objects.all()


    if request.method == "POST":
        record = StudentForm(request.POST)
        if record.is_valid():
            record.save()
        data = Students.objects.all()

    form = StudentForm()

    context = {
        "form" : form,
        "students" : data
    }
    return render(request,'student.html',context)