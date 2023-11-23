from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('anuncio', views.anuncio, name='anuncio'),
    path('anuncio/crear', views.crear, name='crear'),
    path('anuncio/modificar', views.modificar, name='modificar'),
    path('', views.buscador, name='buscador'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('anuncio/modificar/<int:id>', views.modificar, name='modificar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)