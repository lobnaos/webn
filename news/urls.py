from . import views
from django.urls import path

urlpatterns = [
    path('fashion',views.fashion, name='fashion'),
    path('artist',views.artist, name='artist'),
    path('nutrition',views.nutrition, name='nutrition'),
    path('sports',views.sports, name='sports')
]

