from django.shortcuts import render
from designs.models import Design
# Create your views here.
def home(request):
    heroes = Design.objects.filter(is_active=True)
    return render(request, "core/home.html",{"heroes":heroes})