"""vegan_burgers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from reservation.views import get_index, get_menu, reservations_view, make_reservation, edit_reservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name="get_index"),
    path('menu/', get_menu, name="get_menu"),
    path('reservations/', reservations_view, name='reservations_view'),
    path('add-reservation/', make_reservation, name='make_reservation'),
    path('edit-reservation/<int:reservation_id>/,', edit_reservation, name='edit_reservation'),
    path('accounts/', include('allauth.urls')),

]

