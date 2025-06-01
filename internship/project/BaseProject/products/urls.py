from django.urls import path 
from products.views import showProducts

urlpatterns = [
    path('showProducts',showProducts,name='showProducts')
]