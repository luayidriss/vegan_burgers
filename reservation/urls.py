from django.urls import path, include
from . import views

urlpatterns = [
    path('reservations/', views.reservations_view, name='reservations')
]