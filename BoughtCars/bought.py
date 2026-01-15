BOUGHT_CARS_SESSION_KEY = 'bought_cars'

def get_bought_cars(request):
    return request.session.get(BOUGHT_CARS_SESSION_KEY, [])

def add_car_to_bought(request, car_id):
    bought = get_bought_cars(request)
    if car_id not in bought:
        bought.append(car_id)
        request.session[BOUGHT_CARS_SESSION_KEY] = bought
    request.session.modified = True