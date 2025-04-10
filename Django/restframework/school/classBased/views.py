from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize
from classBased.models import Friends
from classBased.serializers import FriendsSeriealizer

class HomeView(APIView):
    def get(self,request):
        data = Friends.objects.all()
        serializer = FriendsSeriealizer(data,many=True) 
        return Response(serializer.data)
    def post(self,request):
        data = request.data #json
        serializer = FriendsSeriealizer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    

