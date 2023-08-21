from django.contrib import admin
from django.urls import path, include
from reservation.views import get_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name="get_index"),
    path('reservation/', include('reservation.urls', namespace='reservation')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('accounts/', include('allauth.urls')),
]