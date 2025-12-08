from django.shortcuts import render

def index(request):
    return render(request, "cars/index.html")

def detail(request, car_id):
    return render(request, "cars/detail.html", {"car_id": car_id})


def about(request):
    return render(request, "cars/about.html")