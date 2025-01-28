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

        if data['age'] < 18:
            raise serializers.ValidationError("Age should be greater than 18")

        return data

