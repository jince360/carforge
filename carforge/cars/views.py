from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def cars(request, car_id):
    selected_car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/cars.html", {"car":selected_car})