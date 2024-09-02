from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    pass

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

