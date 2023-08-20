from django import forms
from django.core.exceptions import ValidationError
from .models import Menu_Item
from django.contrib import messages
from cloudinary.forms import CloudinaryFileField

class Menu_ItemForm(forms.ModelForm):
    item_image = CloudinaryFileField(options={
        'folder': 'menu_item_images',
    })
    class Meta:
        model = Menu_Item
        fields = ['name', 'description', 'category', 'price', 'item_image']
        widgets = {
            'item_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }