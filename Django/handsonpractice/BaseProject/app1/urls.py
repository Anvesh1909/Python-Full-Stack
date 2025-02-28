from django.urls import path

from app1.views import httpResponseView,HttpClassView,homeView,AllStudents,studentView,employeeRegistrationView,getEmployee
from app1.views import setCookie,getCookie,deleteCookie


urlpatterns = [
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
