BOUGHT_CARS_SESSION_KEY = 'bought_cars'

def get_bought_cars(request):
    return request.session.get(BOUGHT_CARS_SESSION_KEY, [])
