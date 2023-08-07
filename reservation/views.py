from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm

def get_index(request):
    return render(request, "index.html")

def get_menu(request):
    return render(request, "menu.html")

def reservations_view(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations.html', context)

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservations_view')
    else:
        form = ReservationForm()

    return render(request, 'add_reservation.html', {'form': form})

