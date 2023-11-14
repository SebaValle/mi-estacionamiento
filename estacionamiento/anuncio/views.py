from django.shortcuts import render
from django.http import HttpResponse
from .models import publicacion

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>hola a todos</h1>")

def inicio2(request):
    return render(request, 'paginas/inicio.html')

def anuncio(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'anuncio/index.html', {'publicaciones': publicaciones})

def crear(request):
    return render(request, 'anuncio/crear.html')

def modificar(request):
    return render(request, 'anuncio/modificar.html')
