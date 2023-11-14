from django.db import models

# Create your models here.

class publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.CharField(max_length=100, verbose_name='dueño')
    horario = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200, verbose_name='descripcion')
    precio = models.CharField(max_length=100, verbose_name='precio')

    def __str__(self):
        fila = "dueño: " + self.dueno + " - " +  "descripcion: " + self.descripcion
        return fila
