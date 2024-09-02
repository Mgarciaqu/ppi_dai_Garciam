from django.db import models
from django.contrib.auth.models import User

class ActividadUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.accion} - {self.fecha}"
