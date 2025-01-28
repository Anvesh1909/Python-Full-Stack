from django.urls import path
from .views import AuthToken, RegisterView, AllStudents, AddStudent, GetStudent

urlpatterns = [
    path("students/", AllStudents.as_view(), name="allStudents"),
    path("students/add/", AddStudent.as_view(), name="addStudent"),
    path("students/<int:pk>/", GetStudent.as_view(), name="getStudent"),
    path("register/", RegisterView.as_view(), name="register"),  # Ensure trailing slash here
    path("auth/", AuthToken.as_view(), name="apiTokenAuth"),
]
