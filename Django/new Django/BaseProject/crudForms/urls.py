from django.urls import path
from crudForms import views

urlpatterns = [
    path('readAll',views.readAll,name="formReadAll"),
    path('update/<int:id>',views.updateStudent,name='formUpdate'),
    path('delete/<int:id>',views.deleteStudent,name='formDelete'),
]
