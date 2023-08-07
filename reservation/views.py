from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reservation

def get_index(request):
    return render(request, "index.html")

def get_menu(request):
    return render(request, "menu.html")

def get_reservation(request):
    return render(request, "reservation.html")

@login_required
def reservations_view(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations.html', context)

