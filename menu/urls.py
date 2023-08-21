from django.urls import path
from .views import menu_view, menu_view_admin, add_menu_item, edit_menu, delete_menu

app_name = 'menu'

urlpatterns = [
    path('menu/', menu_view, name="menu_view"),
    path('admin/', menu_view_admin, name='menu_view_admin'),
    path('add/', add_menu_item, name='add_menu_item'),
    path('edit/<int:menu_item_id>/', edit_menu, name='edit_menu'),
    path('delete/<int:menu_item_id>/', delete_menu, name='delete_menu'),
]
