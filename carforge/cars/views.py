from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def get_model_filters(request):
    """API endpoint to get cities and years filtered by model"""
    model = request.GET.get('model', '')
    
    if model:
        # Filter by the selected model
        cars_for_model = Car.objects.filter(model__iexact=model)
        cities = list(cars_for_model.values_list('city', flat=True).distinct())
        years = list(cars_for_model.values_list('year', flat=True).distinct())
        # Sort years in descending order
        years.sort(reverse=True)
    else:
        # Return all cities and years if no model selected
        cities = list(Car.objects.values_list('city', flat=True).distinct())
        years = list(Car.objects.values_list('year', flat=True).distinct())
        years.sort(reverse=True)
    
    return JsonResponse({
        'cities': cities,
        'years': years
    })

def cars(request, car_id):
    selected_car = get_object_or_404(Car, id=car_id)
    return render(request, "cars/cars.html", {"car":selected_car})

def all_cars(request):
    all_cars = Car.objects.all().order_by("-created_on")
    
    brand = Car.objects.values("brand__name").distinct()
    model = Car.objects.values("model").distinct()
    year = Car.objects.values("year").distinct()
    transmission = Transmission.objects.all()
    fuel = FuelType.objects.all()

    brand_search = request.GET.get("brand")
    model_search = request.GET.get("model")
    year_search = request.GET.get("year")
    transmission_search = request.GET.get("transmission")
    fuel_search = request.GET.get("fuel")
    max_price = request.GET.get("max_price")


    if brand_search:
        all_cars = all_cars.filter(Q(brand__name__iexact=brand_search))
    if model_search:
        all_cars = all_cars.filter(Q(model__iexact=model_search))
    if year_search:
        all_cars = all_cars.filter(Q(year__iexact=year_search))
    if transmission_search:
        all_cars = all_cars.filter(Q(transmission__transmission__iexact=transmission_search))
    if fuel_search:
        all_cars = all_cars.filter(Q(fuel__fuel__iexact=fuel_search))
    if max_price:
        all_cars = all_cars.filter(price__lte=max_price)

    paginator = Paginator(all_cars, 18)
    page = request.GET.get("page")
    paged_car = paginator.get_page(page)
    return render(request, "cars/all_cars.html", {"all_cars":paged_car,"brand":brand, "brand_search":brand_search, "model":model, "model_search":model_search, "year":year, "year_search":year_search, "transmission":transmission, "transmission_search":transmission_search, "fuel":fuel, "fuel_search":fuel_search, "max_price":max_price})

def search_page(request):
    all_cars = Car.objects.all().order_by("-created_on")
    search = request.GET.get("search")
    model_search =request.GET.get("model")
    city_search = request.GET.get("city")
    year_search =request.GET.get("year")
    max_price = request.GET.get("max_price")


    brand = Car.objects.values("brand__name").distinct()
    brand_search = request.GET.get("brand")
    model = Car.objects.values("model").distinct()
    year = Car.objects.values("year").distinct()
    transmission = Transmission.objects.all()
    fuel = FuelType.objects.all()
    transmission_search = request.GET.get("transmission")
    fuel_search = request.GET.get("fuel")
    max_price = request.GET.get("max_price")
    

    if search:
        all_cars = all_cars.filter(Q(brand__name__icontains=search) |Q(color__name__icontains=search) | Q(model__icontains=search))
    if brand_search:
        all_cars = all_cars.filter(Q(brand__name__iexact=brand_search))
    if model_search:
        all_cars = all_cars.filter(Q(model__iexact=model_search))

    if city_search:
        all_cars = all_cars.filter(Q(city__iexact=city_search))

    if year_search:
        all_cars = all_cars.filter(Q(year__iexact=year_search))
    if transmission_search:
        all_cars = all_cars.filter(Q(transmission__transmission__iexact=transmission_search))
    if fuel_search:
        all_cars = all_cars.filter(Q(fuel__fuel__iexact=fuel_search))

    if max_price:
        all_cars = all_cars.filter(price__lte=max_price)
        
    return render(request, "cars/search.html", {"all_cars":all_cars, "model_search":model_search, "city_search":city_search, "max_price":max_price, "brand":brand, "brand_search":brand_search, "model":model, "year":year, "transmission":transmission, "fuel":fuel, "year_search":year_search, "transmission_search":transmission_search, "fuel_search":fuel_search})