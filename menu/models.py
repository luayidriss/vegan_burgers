from django.db import models
from cloudinary.models import CloudinaryField

class Menu_Item(models.Model):
    BURGERS = 'Burgers'
    SIDES = 'Sides'
    DRINKS = 'Drinks'
    DESSERTS = 'Desserts'
    
    CATEGORY_CHOICES = [
        (BURGERS, 'Burgers'),
        (SIDES, 'Sides'),
        (DRINKS, 'Drinks'),
        (DESSERTS, 'Desserts'),
    ]
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=BURGERS)
    item_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"