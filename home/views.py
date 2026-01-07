from django.shortcuts import render
from cars.models import Car
from favorites.favorites import get_favorites_cars

# Create your views here.
def home(request):
    cars = Car.objects.all()[:8]  # Останні 8 автомобілів
    fav_cars = get_favorites_cars(request)
    return render(request, 'home/home.html', {'cars': cars, 'fav_cars': fav_cars})