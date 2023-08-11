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
from reservation.views import get_index, menu_view, reservations_view, make_reservation, edit_reservation, cancel_reservation, menu_view_admin, add_menu_item, edit_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name="get_index"),
    path('menu/', menu_view, name="menu_view"),
    path('reservations/', reservations_view, name='reservations_view'),
    path('make-reservation/', make_reservation, name='make_reservation'),
    path('edit-reservation/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('menu_admin', menu_view_admin, name='menu_view_admin'),
    path('add_menu_item/', add_menu_item, name='add_menu_item'),
    path('edit_menu/', edit_menu, name='edit_menu'),
    path('accounts/', include('allauth.urls')),

]

