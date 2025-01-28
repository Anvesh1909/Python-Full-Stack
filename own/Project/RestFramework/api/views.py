from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Students
from . serializers import StudentSerializer

# Create your views here.

class AddStudent(APIView):
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


class AllStudents(APIView):
    def get(self,request):
        allStudents = Students.objects.all()
        serializer = StudentSerializer(allStudents,many = True)
        return Response(serializer.data)


class GetStudent(APIView):
    def get(self,request,pk):
        student = Students.objects.get(pk = pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def patch(self,request,pk):
        student = Students.objects.get(pk = pk)
        serializer = StudentSerializer(student,data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
        student = Students.objects.get(pk = pk)
        student.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)