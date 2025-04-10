from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize

# api_view is used to convert our view to api_view

# @api_view(['GET'])
# def students(request):
#     return Response("hello")

from student.models import Students

# @api_view(['GET'])
# def students(request):
#     data = Students.objects.all()
#     return Response(data)
# Object of type Students is not JSON serializable

from student.serializers import StudentSerializer

# @api_view(['GET'])
# def students(request):
#     data = Students.objects.all()
#     # convering dict to json
#     # if it more than one use many = tru
#     serializer = StudentSerializer(data,many=True)
#     return Response(serializer.data)


# @api_view(['GET','POST'])
# def students(request):
#     if request.method == 'GET':
#         data = Students.objects.all()
#         # convering dict to json
#         # if it more than one use many = tru
#         serializer = StudentSerializer(data,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data = request.data # json format details 
#         # json to dict
#         serializer = StudentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)




@api_view(['GET','POST','PUT','PATCH','DELETE'])
def students(request):
    if request.method == 'GET':
        data = Students.objects.all()  
        # convering dict to json
        # if it more than one use many = tru
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data # json format details 
        # json to dict
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # if request.method == 'DELETE':
    #     data = request.data # json
    #     std_id = data.get('id')
    #     std = Students.objects.get(id=std_id)
    #     print(std)
    if request.method == 'PUT':
        data = request.data #json
        std = Students.objects.get(id = data.get('id'))   # object
        serializer = StudentSerializer(std, data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'PATCH':
        data = request.data #json
        std = Students.objects.get(id = data.get('id'))   # object
        serializer = StudentSerializer(std, data = data,partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    

@api_view(['GET','DELETE'])
def studentDetails(request,id):
    if request.method == 'GET':
        data = Students.objects.get(id = id)
        # convering dict to json
        serializer = StudentSerializer(data)
        return Response(serializer.data)
    if request.method == 'DELETE':
        std = Students.objects.get(id = id)
        std.delete()
        return Response("Student deleted")