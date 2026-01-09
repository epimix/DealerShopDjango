from django.contrib import admin
from django.urls import path
import cars.views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('cars/',include('cars.urls')),
    path('favorites/',include('favorites.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
