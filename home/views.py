from django.shortcuts import render, get_object_or_404
from cars.models import Car
from favorites.favorites import get_favorites_cars
from django.shortcuts import redirect,render
from BoughtCars.bought import add_car_to_bought

from cars.models import Car, BuyingRequest

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
    add_car_to_bought(request, car_id)
    return redirect('home')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
