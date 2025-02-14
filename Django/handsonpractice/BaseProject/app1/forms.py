from django import forms

class StudentsForm(forms.Form):
    rollNo = forms.IntegerField()
    name = forms.CharField(max_length=200)
    standard = forms.IntegerField()
    presentage = forms.FloatField()

    
class EmployeeRegistration(forms.Form):
    emp_id  = forms.IntegerField()
    name = forms.CharField()
    dept = forms.CharField()
    role = forms.CharField()
    salary = forms.FloatField()
    joining_date = forms.DateField()
    
