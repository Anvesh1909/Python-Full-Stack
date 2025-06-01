from django import forms

from app.models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'status': forms.Select(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter task description'}),
        }