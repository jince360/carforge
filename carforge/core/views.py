from django.shortcuts import render
from designs.models import Design
from cars.models import *
# Create your views here.
def home(request):
    heroes = Design.objects.filter(is_active=True)[:4]
    featured_car = Car.objects.filter(is_featured=True).order_by("-created_on")
    return render(request, "core/home.html",{"heroes":heroes, "featured":featured_car})