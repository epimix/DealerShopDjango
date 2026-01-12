from django.shortcuts import render
from cars.models import Car
from favorites.favorites import get_favorites_cars
from django.shortcuts import redirect,render

from cars.models import Car, BuyingRequest
# Create your views here.
def home(request):
    cars = Car.objects.all()[:8]
    fav_cars = get_favorites_cars(request)
    buying_requests = BuyingRequest.objects.all()
    return render(request, 'home/home.html', {'cars': cars, 'fav_cars': fav_cars, 'buying_requests': buying_requests})



def buy_service(request):
    BuyingRequest.objects.create(
        car_id=Car.objects.first().id,
        customer_name="John Doe",
        customer_phone="123-456-7890",
        message="I'm interested in buying this car."
    )
    return redirect('home')