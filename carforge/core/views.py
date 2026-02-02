from django.shortcuts import render
from designs.models import Design
# Create your views here.
def home(request):
    hero = Design.objects.filter(is_active=True).first()
    return render(request, "core/home.html",{"hero":hero})