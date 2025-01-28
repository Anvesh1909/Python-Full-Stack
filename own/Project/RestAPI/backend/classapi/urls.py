from django.urls import path

from . views import AllStudents,RegisterVIew,LoginView

urlpatterns = [
    path("all/",AllStudents.as_view()),
    path("register/",RegisterVIew.as_view()),
    path("login/",LoginView.as_view())
]
