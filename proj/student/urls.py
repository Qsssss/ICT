from django.urls import path

from student.views import listt

urlpatterns = [
    path('', listt),
]