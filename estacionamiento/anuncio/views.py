from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import publicacion
from .forms import anuncioForm

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>hola a todos</h1>")

def inicio2(request):
    return render(request, 'paginas/inicio.html')

def anuncio(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'anuncio/index.html', {'publicaciones': publicaciones})

def crear(request):
    formulario = anuncioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('anuncio')
    return render(request, 'anuncio/crear.html', {'formulario': formulario})

def modificar(request):
    return render(request, 'anuncio/modificar.html')

def buscador(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'anuncio/buscador.html', {'publicaciones': publicaciones})
