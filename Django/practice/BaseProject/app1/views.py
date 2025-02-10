from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def httpResponseView(request):
    return HttpResponse("This is an HTTP RESPONSE")
    
    
# functional view
def homeView(request):
    return render(request,"home.html")



from django.views import View

# class View
class HomeClassView(View):
    def get(self,request):
        return render(request,"home.html")