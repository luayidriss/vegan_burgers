from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Reservation
from .forms import ReservationForm
from datetime import datetime, timedelta
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_reservation_email(user, reservation, subject_template, email_template):
    subject = render_to_string(subject_template, {'user': user, 'reservation': reservation})
    message = render_to_string(email_template, {'user': user, 'reservation': reservation})
    send_mail(subject.strip(), message, 'your_email@example.com', [user.email], html_message=message)

def get_index(request):
    return render(request, "index.html")

def reservations_view(request):
    now = datetime.now()
    all_reservations = Reservation.objects.filter(user=request.user)
    previous_reservations = all_reservations.filter(date__lt=now)
    upcoming_reservations = all_reservations.filter(date__gte=now)

    context = {
        'all_reservations': all_reservations,
        'previous_reservations': previous_reservations,
        'upcoming_reservations': upcoming_reservations,
    }
    return render(request, 'reservations.html', context)

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()

            send_reservation_email(request.user, reservation, 'make_reservation_subject.txt', 'make_reservation_email.html')
            messages.success(request, 'Reservation successfully made!')
            return redirect('reservation:reservations_view')
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
            form.save()
            if request.user.is_staff:
                send_reservation_email(reservation.user, reservation, 'edit_reservation_subject.txt', 'edit_reservation_email.html')
                messages.success(request, 'Reservation successfully edited!')
                return redirect('reservation:admin_reservations')
            else:
                send_reservation_email(reservation.user, reservation, 'edit_reservation_subject.txt', 'edit_reservation_email.html')
                messages.success(request, 'Reservation successfully edited!')
                return redirect('reservation:reservations_view')
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
            send_reservation_email(reservation.user, reservation, 'cancel_reservation_subject.txt', 'cancel_reservation_email.html')
            messages.success(request, 'Reservation successfully cancelled!')
            return redirect('reservation:admin_reservations')
        else:
            send_reservation_email(reservation.user, reservation, 'cancel_reservation_subject.txt', 'cancel_reservation_email.html')
            messages.success(request, 'Reservation successfully cancelled!')
            return redirect('reservation:reservations_view')

    if request.user.is_staff:
        return redirect('reservation:admin_reservations')
    else:
        return redirect('reservation:reservations_view')

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

