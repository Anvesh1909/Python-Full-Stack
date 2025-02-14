"""
URL configuration for BaseProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from app1.views import httpResponseView,HttpClassView,homeView,AllStudents,studentView,employeeRegistrationView,getEmployee
from app1.views import setCookie,getCookie,deleteCookie

urlpatterns = [
    path("admin/", admin.site.urls),
    path("httpResponse",httpResponseView),
    path("httpClass",HttpClassView.as_view()),
    path("home",homeView),
    path("allStudents",AllStudents.as_view()),
    path("studentForm",studentView),
    path("EmpReg",employeeRegistrationView),
    path("getEmp",getEmployee),
    path("setCookie",setCookie),
    path("getCookie",getCookie),
    path("deleteCookie",deleteCookie),
]
