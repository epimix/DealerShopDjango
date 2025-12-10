from django.contrib import admin
from django.urls import path
import cars.views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',include('cars.urls')),

]
