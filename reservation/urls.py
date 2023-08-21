from django.urls import path
from .views import get_index, reservations_view, make_reservation, edit_reservation, cancel_reservation, admin_reservations

app_name = 'reservation'

urlpatterns = [
    path('', reservations_view, name='reservations_view'),
    path('add', make_reservation, name='make_reservation'),
    path('edit/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('admin-dashboard/', admin_reservations, name='admin_reservations'),
]