from django import forms
from crudForms.models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        # fields = ['name','age','course']