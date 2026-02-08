from django.urls import path
from .views import *

urlpatterns = [
    path("cars/<int:car_id>/",cars, name="cars"),
    path("all_cars/", all_cars, name="all_cars"),
    path("search/", search_page, name="search"),
    path("api/model-filters/", get_model_filters, name="get_model_filters"),
]
