from django.urls import path
from .views import calculate_bmi

urlpatterns = [
    path('', calculate_bmi, name='calculate_bmi'),
]
