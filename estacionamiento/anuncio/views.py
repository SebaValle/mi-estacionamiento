from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import publicacion
from .forms import anuncioForm
from django.db.models import Q
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

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

def modificar(request, id):
    publicaciones = publicacion.objects.get(id=id)
    formulario = anuncioForm(request.POST or None, request.FILES or None, instance=publicaciones)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('anuncio')
    return render(request, 'anuncio/modificar.html', {'formulario': formulario})

def buscador(request):
    queryset = request.GET.get("buscar")
    publicaciones = publicacion.objects.all()
    if queryset:
        publicaciones = publicacion.objects.filter(
            Q(dueno__icontains = queryset) |
            Q(horario__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(precio__icontains = queryset)
        ).distinct()
    return render(request, 'anuncio/buscador.html', {'publicaciones': publicaciones})

def eliminar(request, id):
    publicaciones = publicacion.objects.get(id=id)
    publicaciones.delete()
    return redirect('anuncio')

def examinar(request, id):
    publicacion_actual = publicacion.objects.get(id=id)

    if request.method == 'POST':
        if 'arrendar' in request.POST:
            publicacion_actual.estado = 'ocupado'
        elif 'cancelar' in request.POST:
            publicacion_actual.estado = 'libre'

        publicacion_actual.save()

    return render(request, 'anuncio/examinar.html', {'publicacion_actual': publicacion_actual})

def login(request):
    publicaciones = publicacion.objects.all()
    return render(request, 'anuncio/login.html', {'publicaciones': publicaciones})

def registro(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            password = formulario.cleaned_data.get('password')
            usuario.set_password(password)
            usuario.save()
            login(request, usuario)
            return redirect('anuncio')  # Redirige a la página que desees después del registro
    else:
        formulario = RegistroForm()

    return render(request, 'login/registro.html', {'formulario': formulario})