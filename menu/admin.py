from django.contrib import admin
from .models import Menu_Item

class MenuItemAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'price')
    search_fields = ['name']
admin.site.register(Menu_Item, MenuItemAdmin)

