from django.shortcuts import render
from designs.models import Design
from cars.models import *
# Create your views here.
def home(request):
    heroes = Design.objects.filter(is_active=True)[:4]
    featured_car = Car.objects.filter(is_featured=True).order_by("-created_on")
    all_cars = Car.objects.all().order_by("-created_on")
    search_models = Car.objects.values("model", "brand__name").distinct()
    search_cities = Car.objects.values("city").distinct()
    search_year = Car.objects.values("year").distinct()

    return render(request, "core/home.html",{"heroes":heroes, "featured":featured_car, "all_cars":all_cars,"search_models":search_models, "search_cities":search_cities,"year":search_year})