from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>hola a todos</h1>")
def inicio2(request):
    return render(request, 'paginas/inicio.html')
def anuncio(request):
    return render(request, 'anuncio/index.html')
