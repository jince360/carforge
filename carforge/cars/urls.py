from django.urls import path
from .views import *

urlpatterns = [
    path("cars/<int:car_id>/",cars, name="cars"),
    path("all_cars", all_cars, name="all_cars"),
]
