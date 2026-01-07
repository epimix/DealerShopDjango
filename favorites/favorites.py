FAVORITES_SESSION_KEY = 'favorites_cars'

def get_favorites_cars(request):
    return request.session.get(FAVORITES_SESSION_KEY, [])

def get_count_of_favorites_cars(request):
    return len(get_favorites_cars(request))


def add_car_to_favorites(request, car_id):
    favorites = get_favorites_cars(request)
    if car_id not in favorites:
        favorites.append(car_id)
        request.session[FAVORITES_SESSION_KEY] = favorites
    request.session.modified = True

def remove_car_from_favorites(request, car_id):
    favorites = get_favorites_cars(request)
    if car_id in favorites:
        favorites.remove(car_id)
        request.session[FAVORITES_SESSION_KEY] = favorites
    request.session.modified = True