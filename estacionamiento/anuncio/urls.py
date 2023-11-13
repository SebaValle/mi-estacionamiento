from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('', views.inicio2, name='inicio2'),
    path('anuncio', views.anuncio, name='anuncio'),
    path('anuncio/crear', views.crear, name='crear'),
    path('anuncio/modificar', views.modificar, name='modificar'),
]