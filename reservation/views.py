from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation, Menu_Item
from .forms import ReservationForm

def get_index(request):
    return render(request, "index.html")

def menu_view(request):
    menu_items_by_category = {}
    
    menu_items = Menu_Item.objects.all()
    
    for category, _ in Menu_Item.CATEGORY_CHOICES:
        items = menu_items.filter(category=category)
        menu_items_by_category[category] = items
    
    context = {
        'menu_items_by_category': menu_items_by_category,
    }
    return render(request, 'menu.html', context)

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

    return render(request, 'make_reservation.html', {'form': form})

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations_view')

    else:
        form = ReservationForm(instance=reservation)

    context = {'form': form}
    return render(request, 'edit_reservation.html', context)

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations_view')

    return redirect('reservations_view')

