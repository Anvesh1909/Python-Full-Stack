from django import forms
from task.models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        # fields = '__all__'
        fields = ['title','description','status']