from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from . serializers import StudentSerializer, RegisterSerializer, LoginSerializer
from . models import StudentTable


from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegisterVIew(APIView):

    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = authenticate(username = serializer.data["username"] , password = serializer.data["password"])
            token, _ = Token.objects.get_or_create(user = user)
            return Response({"Token" : token.key },status=status.HTTP_201_CREATED)
        
        return Response({"message" : "bad request invalid credintials"})



class AllStudents(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    # Authorization : Token 1d12c3c99dabc5305f077e4992b30e24f4d91d21

    def get(self,request):
        print(request.user)
        id = request.data.get("id")
        if id:
            obj = StudentTable.objects.get(id = id)
            serializer = StudentSerializer(obj)
        else:
            obj = StudentTable.objects.all()
            serializer = StudentSerializer(obj,many = True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request):
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        serializer = StudentSerializer(obj,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializere.errors)

    def patch(self,request):
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        serializer = StudentSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

    def delete(self,request):
        data = request.data
        obj = StudentTable.objects.get(id = request.data.get('id'))
        obj.delete()
        return Response({'message':'deleted successfully'})