from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','category','brand','price','stock','is_available','image']
    list_editable = ['name','description','category','brand','price','stock','is_available','image']


admin.site.register(Product,ProductAdmin)