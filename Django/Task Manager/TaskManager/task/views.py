from django.http import HttpResponse
from django.shortcuts import render,redirect

from task.models import Tasks
from task.forms import TaskForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        formData = TaskForm(request.POST)
        if formData.is_valid():
            task = formData.save(commit=False)  
            task.user = request.user  
            task.save()  

    data = Tasks.objects.filter(user=request.user)  

    context = {
        'tasks': data,
        'taskForm': TaskForm(),
        'user': request.user
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def update(request,id):
    data = Tasks.objects.get(id=id)

    if request.method == "POST":
        formData = TaskForm(request.POST,instance = data)
        if formData.is_valid():
            formData.save()
        return redirect('home')


    update_Form = TaskForm(instance = data)
    
    context = {
        'taskForm': update_Form
    }
    return render(request,'index.html',context)


@login_required(login_url='login')
def delete(request,id):
    data = Tasks.objects.get(id=id)
    data.delete()
    return redirect('home')



def loginUser(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
            message = "Username or password is incorrect"

    context = {
        'message' : message
    }

    return render(request,'login.html',context)

def signupUser(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('confirmpassword')
        # print(username,email,p1,p2)
        if p1==p2:
            try:
                user = User.objects.create_user(username,email,p1)
                user.save()
                return redirect('login')
            except Exception as e:
                message = 'username already exists'
        else:
            message = 'password not equal to confirm password'

    context = {
        'message' : message
    }

    return render(request,'signup.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')