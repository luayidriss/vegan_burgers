from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Sum
from datetime import datetime, time
from .models import Reservation, Menu_Item

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].label = "Email"
        self.fields['password2'].label = "Confirm Password"
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['placeholder'] = ''

    def save(self, request):
        user = super().save(request)
        return user

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'guests']
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.now().date():
            raise ValidationError("Reservation date must be in the future.")
        return date
        
    def clean_time(self):
        time_value = self.cleaned_data.get('time')
        date = self.cleaned_data.get('date')

        if not date:
            return time_value

        day_of_week = date.weekday()

        opening_time_weekdays = time(16, 0)
        closing_time_weekdays = time(21, 0)
        opening_time_weekends = time(13, 0)
        closing_time_weekends = time(21, 0)

        if 0 <= day_of_week <= 3:
            if not (opening_time_weekdays <= time_value <= closing_time_weekdays):
                raise ValidationError("Reservation time must be within working hours.")
        else:
            if not (opening_time_weekends <= time_value <= closing_time_weekends):
                raise ValidationError("Reservation time must be within working hours.")
        return time_value

    def clean_guests(self):
        number_of_guests = self.cleaned_data.get('guests')
        date = self.cleaned_data.get('date')

        if number_of_guests and date is not None:
            total_guests = Reservation.objects.filter(date=date).aggregate(Sum('guests'))['guests__sum'] or 0
            restaurant_capacity = 40

            if total_guests + number_of_guests > restaurant_capacity:
                raise ValidationError("This reservation exceedes restaurant capacity for that day.")
                
        return number_of_guests


class Menu_ItemForm(forms.ModelForm):
    class Meta:
        model = Menu_Item
        fields = ['name', 'description', 'category', 'price', 'item_image']
