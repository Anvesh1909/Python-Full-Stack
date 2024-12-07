from django.shortcuts import render,redirect
from . models import basics


# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName') or 'NA'
        
        basics.objects.create(
            firstName=first_name,
            lastName=last_name
        )  
    

    context = {
        'details': basics.objects.all()
    }

    return render(request, 'index.html', context)


def delete(request):
    if request.method == "POST":
        id = request.POST.get("id")
        c = basics.objects.get(id = id)
        c.delete()
    return redirect('index')


def update(request,id):
    c = basics.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName') or 'NA'
        
        c.firstName = first_name
        c.lastName = last_name
        c.save()
        
        return redirect('index')
    
    context = {
        'update': c
    }

    return render(request,'update.html',context)