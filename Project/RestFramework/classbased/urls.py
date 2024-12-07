from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update/<int:id>/', Update.as_view(), name='get'),
    path('delete', Delete.as_view(), name='get')

]
