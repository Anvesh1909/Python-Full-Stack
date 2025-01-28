
from django.urls import path
from . views import *

urlpatterns = [
    path("",AllStudents.as_view(),name= "allStudents"),
    path("post",AddStudent.as_view(),name = "addStudent"),
    path("get/<int:pk>",GetStudent.as_view(),name = "getStudent"),
    path("update/<int:pk>",GetStudent.as_view(),name = "updateStudent"),
    path("delete/<int:pk>",GetStudent.as_view(),name = "deleteStudent"),
]
