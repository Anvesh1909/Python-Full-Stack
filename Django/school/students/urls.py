
from django.urls import path
from students.views import IndexView

urlpatterns = [
    path('home',IndexView.as_view()),
]
