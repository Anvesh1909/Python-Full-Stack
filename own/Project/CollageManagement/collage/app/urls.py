from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Department/', views.DepartmentView, name='Department'),
    path('Teachers/', views.TeachersView, name='Teachers'),
    path('TeacherProfile/', views.TeacherProfileView, name='TeacherProfile'),
    path('Subject/', views.SubjectView, name='Subject'),
    path('Student/', views.StudentView, name='Student'),
    path('StudentSubjects/', views.StudentSubjectsView, name='StudentSubjects'),
    path('Library/', views.LibraryFormView, name='Library')
]
