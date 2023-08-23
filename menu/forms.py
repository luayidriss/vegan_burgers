from django import forms
from django.core.exceptions import ValidationError
from .models import MenuItem
from django.contrib import messages
from cloudinary.forms import CloudinaryFileField

class MenuItemForm(forms.ModelForm):
    item_image = CloudinaryFileField(options = {
        'folder': 'menu_item_images',
    })
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'category', 'price', 'item_image']
        widgets = {
            'item_image': forms.FileInput(attrs = {'accept': 'image/*'}),
     }