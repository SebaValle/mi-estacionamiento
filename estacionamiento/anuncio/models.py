from django.db import models

# Create your models here.

class publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.CharField(max_length=100, verbose_name='dueño')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='imagen', null=True)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300, verbose_name='descripcion')
    precio = models.CharField(max_length=100, verbose_name='precio')
    estado = models.CharField(max_length=100, verbose_name='estado', default='libre')

    def __str__(self):
        fila = "dueño: " + self.dueno + " - " +  "descripcion: " + self.descripcion
        return fila
