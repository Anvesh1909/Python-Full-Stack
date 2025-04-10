from django.urls import path
from crud import views

urlpatterns = [
    path('readAll',views.readAll,name="readAll"),
    path('update/<int:id>',views.updateStudent,name='update'),
    path('delete/<int:id>',views.deleteStudent,name='delete'),
]
