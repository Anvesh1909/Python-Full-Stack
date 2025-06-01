from django.urls import path

from . import views

urlpatterns = [
    path('allProducts',views.productsView,name='allProducts'),
    path('category',views.categoryView,name='category'),
]