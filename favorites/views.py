from django.shortcuts import render, redirect
from django.urls import reverse
from cars.models import Car
from favorites.favorites import add_car_to_favorites, get_favorites_cars, remove_car_from_favorites

def index(request):
    cars = Car.objects.all()
    favorites = get_favorites_cars(request)
    cars = [car for car in cars if car.id in favorites]
    return render(request, 'favorites/index.html', {'cars': cars})

def add_car(request, car_id, return_url):
    add_car_to_favorites(request, car_id)
    # Map common return URL names to actual URLs
    url_map = {
        'car_index': '/cars/',
        'car_detail': f'/cars/{car_id}/',
        'favorites:index': '/favorites/',
        'home': '/',
        'index': '/cars/',
    }
    # Handle URL names with colons (app:name format)
    if ':' in return_url:
        try:
            redirect_url = reverse(return_url)
        except:
            redirect_url = url_map.get(return_url, '/cars/')
    else:
        redirect_url = url_map.get(return_url, return_url)
    if not redirect_url.startswith('/'):
        redirect_url = '/' + redirect_url
    return redirect(redirect_url)

def remove_car(request, car_id, return_url):
    remove_car_from_favorites(request, car_id)
    # Map common return URL names to actual URLs
    url_map = {
        'car_index': '/cars/',
        'car_detail': f'/cars/{car_id}/',
        'favorites:index': '/favorites/',
        'home': '/',
        'index': '/cars/',
    }
    # Handle URL names with colons (app:name format)
    if ':' in return_url:
        try:
            redirect_url = reverse(return_url)
        except:
            redirect_url = url_map.get(return_url, '/cars/')
    else:
        redirect_url = url_map.get(return_url, return_url)
    if not redirect_url.startswith('/'):
        redirect_url = '/' + redirect_url
    return redirect(redirect_url)
