from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from cars.forms import CarForm
from cars.models import Car
from django.contrib import messages

# cars = [
#     {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020, "price": 24000},
#     {"id": 2, "brand": "Honda", "model": "Accord", "year": 2019, "price": 22000},
#     {"id": 3, "brand": "Ford", "model": "Mustang", "year": 2021, "price": 26000},
#     {"id": 4, "brand": "Chevrolet", "model": "Malibu", "year": 2018, "price": 21000},
#     {"id": 5, "brand": "Nissan", "model": "Altima", "year": 2022, "price": 25000},
# ]

from favorites.favorites import get_count_of_favorites_cars, get_favorites_cars


def car_index(request):
    cars = Car.objects.all()
    return render(request, "cars/index.html", {"cars": cars, "fav_count": get_count_of_favorites_cars(request), "fav_cars": get_favorites_cars(request)})

def carsList(request):
    cars = Car.objects.all()
    messages.success(request, "Cars fetched successfully")
    return render(request, "cars/list.html", {"cars": cars})


def carDetail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    fav_cars = get_favorites_cars(request)
    return render(request, "cars/detail.html", {"car": car, "fav_cars": fav_cars})


def deleteCar(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()    
    messages.success(request, "Car deleted successfully")
    return redirect("/cars/list")


def createCar(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save()
            messages.success(request, "Car created successfully")
            return redirect(reverse("car_detail", args=[car.id]))
    else:
        form = CarForm()

    return render(request, "cars/create.html", {"form": form})

def editCar(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save()
            messages.success(request, "Car updated successfully")
            return redirect(reverse("car_detail", args=[car.id]))
    else:
        form = CarForm(instance=car)

    return render(request, "cars/edit.html", {"form": form, "car": car})