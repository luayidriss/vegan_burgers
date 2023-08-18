from django import forms
from django.core.exceptions import ValidationError
from .models import Menu_Item
from django.contrib import messages

class Menu_ItemForm(forms.ModelForm):
    class Meta:
        model = Menu_Item
        fields = ['name', 'description', 'category', 'price', 'item_image']