from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='collage'),  # Root URL for the index page
    path('department/', views.DepartmentView, name='department'),  # URL for the department view
]
