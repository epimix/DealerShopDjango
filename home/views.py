from django.shortcuts import render, get_object_or_404
from cars.models import Car
from favorites.favorites import get_favorites_cars
from django.shortcuts import redirect,render
from BoughtCars.bought import add_car_to_bought

from cars.models import Car, BuyingRequest
# Create your views here.
def home(request):
    cars = Car.objects.all()[:8]
    fav_cars = get_favorites_cars(request)
    buying_requests = BuyingRequest.objects.all()
    return render(request, 'home/home.html', {'cars': cars, 'fav_cars': fav_cars, 'buying_requests': buying_requests})



def buy_service(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    BuyingRequest.objects.create(
        car=car,
        customer_name="customer"
    )
    # Add car to bought cars session
    add_car_to_bought(request, car_id)
    return redirect('home')