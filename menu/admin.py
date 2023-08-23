from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'price')
    search_fields = ['name']
admin.site.register(MenuItem, MenuItemAdmin)

