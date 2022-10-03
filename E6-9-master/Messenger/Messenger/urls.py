from django.urls import path, include
from django.contrib import admin
from room.views import *


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('rooms/', include('room.urls')),
    path('create/', room_create, name='room_create'),
]