from django.shortcuts import render, redirect, get_object_or_404
from .models import BoughtCar
from cars.models import Car
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    bought_cars = BoughtCar.objects.filter(user=request.user)
    cars = [b.car for b in bought_cars]
    return render(request, 'bought/index.html', {'cars': cars})

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if not BoughtCar.objects.filter(user=request.user, car=car).exists():
        BoughtCar.objects.create(user=request.user, car=car)
    return redirect('bought:index')



