from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time} - {self.guests}"


class Menu_Item(models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    item_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"
