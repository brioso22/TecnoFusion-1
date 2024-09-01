from django.db import models
from tienda.models import Producto  
from inicio.models import Empleado, Sucursal  

class Donacion(models.Model):
    num_equipo = models.CharField(max_length=100)
    donador = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True, related_name='donaciones')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='donaciones')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True, related_name='donaciones')

    def __str__(self):
        return f"Donación {self.num_equipo} - {self.donador}"
