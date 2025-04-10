# from django import forms
from attr import field
from rest_framework import serializers

from student.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields = ['name','present','phoneNo']
        fields = '__all__'