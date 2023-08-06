from django.shortcuts import render

def get_index(request):
    return render(request, "index.html")

def get_menu(request):
    return render(request, "menu.html")

def get_reservation(request):
    return render(request, "reservation.html")

