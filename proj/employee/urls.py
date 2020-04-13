from django.urls import path

from employee.views import listt

urlpatterns = [
    path('', listt),
]