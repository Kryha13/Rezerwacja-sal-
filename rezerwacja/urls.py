"""rezerwacja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking.views import room, new_room, delete_room, room_details, modify_room, book_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', room),
    path('room/new', new_room),
    path('room/delete', delete_room),
    path('room/details/<int:room_id>', room_details),
    path('room/modify/<int:room_id>', modify_room),
    path('room/book/<int:room_id>', book_room),

]
