from django.contrib import admin
from ORM.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','email']

admin.site.register(Employee,EmployeeAdmin)