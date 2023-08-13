from allauth.account.forms import SignupForm
from django import forms
from datetime import datetime
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
    
    def validate_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.now().date():
            raise ValidationError("Reservation date must be in the future.")
        return date

class Menu_ItemForm(forms.ModelForm):
    class Meta:
        model = Menu_Item
        fields = ['name', 'description', 'category', 'price', 'item_image']
