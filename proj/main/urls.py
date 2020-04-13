from django.urls import path

from main.views import listt

urlpatterns = [
    path('', listt),
]