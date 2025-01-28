from django import forms
from .models import *

# Department Form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}),
        }

# Teachers Form
class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Teacher Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

# TeacherProfile Form
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),  
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Subject Form
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Name'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

# StudentSubjects Form
class StudentSubjectsForm(forms.ModelForm):
    class Meta:
        model = StudentSubjects  
        fields = '__all__'
        widgets = {
            'Subject': forms.Select(attrs={'class': 'form-control'}),  
            'Student': forms.Select(attrs={'class': 'form-control'}),
        }

# Library Form
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'
        widgets = {
            'book': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Title'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'returned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
