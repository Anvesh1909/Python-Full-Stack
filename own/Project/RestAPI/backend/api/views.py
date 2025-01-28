from rest_framework.decorators import api_view 
from rest_framework.response import Response

from . serializers import StudentSerializer
from . models import StudentTable

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def allStudents(request):

    if request.method == 'GET':
        id = request.data.get("id")
        if id:
            obj = StudentTable.objects.get(id = id)
            serializer = StudentSerializer(obj)
        else:
            obj = StudentTable.objects.all()
            serializer = StudentSerializer(obj,many = True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        serializer = StudentSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializere.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        serializer = StudentSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)   

    elif request.method == 'DELETE':
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        obj.delete()
        return Response({'message':'deleted successfully'})