from rest_framework import serializers
from . models import StudentTable

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTable
        fields = '__all__'

    
    def validate(self,data):

        specialCharecter = '~`!@#$%^&*()_-+=}]{[:;/.,'

        for i in data['name']:
            if i in  specialCharecter:
                raise serializers.ValidationError("dont use special charecters")

        if data.get('age') and data['age'] < 18:
            raise serializers.ValidationError("Age should be greater than 18")

        return data



from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        if data.get('username'):
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username already taken")
            
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("email already taken")


        return data


    def create(self,validated_data):
        user = User.objects.create(username= validated_data["username"],email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return validated_data




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    