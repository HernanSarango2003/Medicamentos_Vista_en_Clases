from django.db import models
from django.contrib.auth.models import User
class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    estado = models.BooleanField(default=True)  # Activo/Inactivo
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
