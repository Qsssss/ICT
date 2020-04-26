from django.urls import path
from student.views import *

urlpatterns = [
    path('', menu),
    path('private/', private_data),
    path('app/', application),
    path('get_card/', get_card),
    path('registration/', registration),
    path('academic/', academic_mobility),
    path('payment/', payment),
    path('answers/', answers),
    path('app/blank/', categories_list),
]