from django.contrib import admin
from django.urls import path
import cars.views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
import home.views

urlpatterns = [
    path('', include('home.urls')),
    path('signup/', home.views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('cars/',include('cars.urls')),
    path('favorites/',include('favorites.urls')),
    path('bought/', include('BoughtCars.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
