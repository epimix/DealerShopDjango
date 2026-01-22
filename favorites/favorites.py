from .models import Favorite

FAVORITES_SESSION_KEY = 'favorites_cars'

def get_favorites_cars(request):
    if request.user.is_authenticated:
        return list(Favorite.objects.filter(user=request.user).values_list('car_id', flat=True))
    return request.session.get(FAVORITES_SESSION_KEY, [])

def get_count_of_favorites_cars(request):
    return len(get_favorites_cars(request))


def add_car_to_favorites(request, car_id):
    if request.user.is_authenticated:
        Favorite.objects.get_or_create(user=request.user, car_id=car_id)
    else:
        favorites = get_favorites_cars(request)
        if car_id not in favorites:
            favorites = list(favorites)     
            favorites.append(car_id)
            request.session[FAVORITES_SESSION_KEY] = favorites
            request.session.modified = True

def remove_car_from_favorites(request, car_id):
    if request.user.is_authenticated:
        Favorite.objects.filter(user=request.user, car_id=car_id).delete()
    else:
        favorites = get_favorites_cars(request)
        if car_id in favorites:
            favorites = list(favorites) 
            favorites.remove(car_id)
            request.session[FAVORITES_SESSION_KEY] = favorites
            request.session.modified = True