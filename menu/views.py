from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Menu_Item
from .forms import Menu_ItemForm
from django.contrib import messages
from cloudinary.uploader import upload

def menu_view(request):
    menu_items_by_category = {}
    
    menu_items = Menu_Item.objects.all()
    
    for category, _ in Menu_Item.CATEGORY_CHOICES:
        items = menu_items.filter(category=category)
        menu_items_by_category[category] = items
    
    context = {
        'menu_items_by_category': menu_items_by_category,
    }
    return render(request, 'menu.html', context)

def menu_view_admin(request):
    menu_items_by_category = {}
    
    menu_items = Menu_Item.objects.all()
    
    for category, _ in Menu_Item.CATEGORY_CHOICES:
        items = menu_items.filter(category=category)
        menu_items_by_category[category] = items
    
    context = {
        'menu_items_by_category': menu_items_by_category,
    }
    return render(request, 'menu_admin.html', context)

def add_menu_item(request):
    form = Menu_ItemForm()
    if request.method == 'POST':
        form = Menu_ItemForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.save()
            messages.success(request, 'Menu Item successfully added!')
            return redirect('menu_view_admin')

    context = {'form': form}
    return render(request, 'add_menu.html', context)

def edit_menu(request, menu_item_id):
    menu_item = get_object_or_404(Menu_Item, id=menu_item_id)

    if request.method == 'POST':
        form = Menu_ItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu Item successfully edited!')
            return redirect('menu_view_admin')

    else:
        form = Menu_ItemForm(instance=menu_item)

    context = {'form': form}
    return render(request, 'edit_menu.html', context)

def delete_menu(request, menu_item_id):
    menu_item = get_object_or_404(Menu_Item, id=menu_item_id)

    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, 'Menu Item successfully deleted!')
        return redirect('menu_view_admin')

    return redirect('menu_view_admin')
