from django.contrib import admin

# Register your models here.
from app1.models import Employees,Reporter,Artical

admin.site.register(Employees)
admin.site.register(Reporter)
admin.site.register(Artical)
