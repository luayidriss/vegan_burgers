from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'date', 'time', 'guests')
    search_fields = ['user']
admin.site.register(Reservation, ReservationAdmin)
