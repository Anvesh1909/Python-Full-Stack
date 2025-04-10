from django.contrib import admin

from products.models import Products

# Register your models here.

# directly access the table in the admin panal 
# admin.site.register(Products)

# customization in django admin 
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','is_published','created_at','modified_at')
    list_display_links = ('id','name')
    list_filter = ('price','created_at')
    list_editable = ('is_published',)
    search_fields  = ('name','price')
    ordering = ('price',)
    # exclude = ('discription',)

admin.site.register(Products,ProductsAdmin)