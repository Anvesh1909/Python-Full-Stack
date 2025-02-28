from django.shortcuts import render

# Create your views here.
from transfer.models import Users
from transfer.forms import UserForm

def transferData(request):
    form = UserForm()
    if request.method == "POST":
        data = UserForm(request.POST)
        if form.is_valid():
            data.save()

    context = {
        "form" : form 
    }

    return render(request, "transfer.html",context)



from django.views import View

class TransferData(View):
    def get(self,request):
        form = UserForm()

        context = {
            "form" : form 
        }
        
        return render(request, "transfer.html",context)
        

    def post(self,request):
        form = UserForm()
        if request.method == "POST":
            data = UserForm(request.POST)
            if form.is_valid():
                data.save()

        context = {
            "form" : form 
        }
        
        return render(request, "transfer.html",context)