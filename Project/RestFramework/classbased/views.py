from django.shortcuts import render,redirect,get_object_or_404
from . models import basics
from django.views.generic import View


class IndexView(View):

    def post(self,request):
        firstname = request.POST.get("FirstName")
        lastname = request.POST.get("LastName")
        basics.objects.create(firstName=firstname, lastName = lastname)   

        return redirect('index')
    
    def get(self,request):
        context = {
            "details" : basics.objects.all()
        }

        return render(request,'index.html',context)

class Update(View):

        def get(self,request,id):
            context = {
                'update' : basics.objects.get(id = id)
            }
            return render(request,"update.html",context)
        
        def post(self,request,id):
            name = basics.objects.get(id = id)
            name.firstName = request.POST.get("FirstName")
            name.lastName = request.POST.get("LastName")
            name.save()
            return redirect('index')


class Delete(View):

    def post(self,request):
        id = request.POST.get("id")
        obj = basics.objects.get(id= id)
        obj.delete()
        return redirect('index')