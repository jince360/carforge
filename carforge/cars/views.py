from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.
def cars(request, car_id):
    selected_car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/cars.html", {"car":selected_car})

def all_cars(request):
    all_cars = Car.objects.all().order_by("-created_on")
    paginator = Paginator(all_cars, 18)
    page = request.GET.get("page")
    paged_car = paginator.get_page(page)
    return render(request, "cars/all_cars.html", {"all_cars":paged_car})