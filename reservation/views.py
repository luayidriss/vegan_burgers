from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Reservation, Menu_Item
from .forms import ReservationForm, Menu_ItemForm
from datetime import datetime, timedelta
from django.contrib import messages

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
            messages.success(request, 'Reservation successfully made!')
            return redirect('reservations_view')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = ReservationForm()

    return render(request, 'make_reservation.html', {'form': form})

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            print("VALID!!!!!!!!")
            form.save()
            if request.user.is_staff:
                messages.success(request, 'Reservation successfully edited!')
                return redirect('admin_reservations')
            else:
                messages.success(request, 'Reservation successfully edited!')
                return redirect('reservations_view')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = ReservationForm(instance=reservation)

    context = {'form': form}
    return render(request, 'edit_reservation.html', context)

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.delete()
        if request.user.is_staff:
            messages.success(request, 'Reservation successfully cancelled!')
            return redirect('admin_reservations')
        else:
            messages.success(request, 'Reservation successfully cancelled!')
            return redirect('reservations_view')

    if request.user.is_staff:
        return redirect('admin_reservations')
    else:
        return redirect('reservations_view')

def menu_view_admin(request):
    menu_items_by_category = {}
    
    menu_items = Menu_Item.objects.all()
    
    for category, _ in Menu_Item.CATEGORY_CHOICES:
        items = menu_items.filter(category=category)
        menu_items_by_category[category] = items
    
    context = {
        'menu_items_by_category': menu_items_by_category,
    }
    return render(request, 'menu_admin.html', context)

def add_menu_item(request):
    form = Menu_ItemForm()
    if request.method == 'POST':
        form = Menu_ItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.save()
            messages.success(request, 'Menu Item successfully added!')
            return redirect('menu_view_admin')

    context = {'form': form}
    return render(request, 'add_menu.html', context)

def edit_menu(request, menu_item_id):
    menu_item = get_object_or_404(Menu_Item, id=menu_item_id)

    if request.method == 'POST':
        form = Menu_ItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu Item successfully edited!')
            return redirect('menu_view_admin')

    else:
        form = Menu_ItemForm(instance=menu_item)

    context = {'form': form}
    return render(request, 'edit_menu.html', context)

def delete_menu(request, menu_item_id):
    menu_item = get_object_or_404(Menu_Item, id=menu_item_id)

    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, 'Menu Item successfully deleted!')
        return redirect('menu_view_admin')

    return redirect('menu_view_admin')

def admin_reservations(request):
    now = datetime.now()

    archived_reservations = Reservation.objects.filter(date__lt=now - timedelta(days=30))
    previous_reservations = Reservation.objects.filter(date__gte=now - timedelta(days=30), date__lt=now)
    upcoming_reservations = Reservation.objects.filter(date__gte=now)

    reservations_by_category = {
        'Archived': archived_reservations,
        'Previous': previous_reservations,
        'Upcoming': upcoming_reservations,
    }

    context = {
        'reservations_by_category': reservations_by_category,
    }

    return render(request, 'reservations_admin.html', context)

