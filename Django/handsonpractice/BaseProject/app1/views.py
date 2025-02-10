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
