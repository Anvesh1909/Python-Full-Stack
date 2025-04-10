from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def indexView(request):
    # print(request.user)
    context = {
        'user' : request.user
    }  
    return render(request,'index.html',context)

def loginUser(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            # context = {
            #     'message' : 'username or password is incorrect'
            # }
            # return render(request,'login.html',context)
            message = 'username or password is incorrect'
    context = {
        'message' : message
    }
        
    return render(request,'login.html',context)

def signUpUser(request):

    message = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('ConfirmPassword')

        # print(username,email,p1,p2)
        if p1==p2:
            try:
                user = User.objects.create_user(username,email,p1)
                user.save()
                return redirect('login')
            except Exception as e:
                message = f'{username} user already exists'
        else:
            # context = {
            #     'message' : 'password not equal to confirm password'
            # }
            # return render(request,'signup.html',context)

            message = 'password not equal to confirm password'

    context = {
        'message' : message
    }

    return render(request,'signup.html',context)


def logoutUser(request):
    logout(request)
    return redirect('index')