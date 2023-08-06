from django.contrib import admin
from .models import Reservation, Menu_Item

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'date', 'time', 'guests')
    search_fields = ['user']
admin.site.register(Reservation, ReservationAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'price')
    search_fields = ['name']
admin.site.register(Menu_Item, MenuItemAdmin)
