from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

class IndexClass(View):
    '''
        "get","post","put","patch","delete","head","options","trace",
    '''
    def get(self,request):
        return HttpResponse("<h1>Class Component Get</h1>")
        
        