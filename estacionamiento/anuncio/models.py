from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

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
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='nombre')
    apellido = models.CharField(max_length=30, verbose_name='apellido')
    correo = models.EmailField(unique=True, verbose_name='correo')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='usuarios',  # Cambiado el related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='usuarios',  # Cambiado el related_name
    )


    def __str__(self):
        return self.username
