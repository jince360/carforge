from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def cars(request, car_id):
    selected_car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/cars.html", {"car":selected_car})

def all_cars(request):
    all_cars = Car.objects.all().order_by("-created_on")
    return render(request, "cars/all_cars.html", {"all_cars":all_cars})