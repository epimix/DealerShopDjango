from favorites.favorites import get_count_of_favorites_cars

def favorites_cars_count(request):
    return { 'fav_count': get_count_of_favorites_cars(request) }