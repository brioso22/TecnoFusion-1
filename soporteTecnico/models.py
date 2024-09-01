from django.db import models
from tienda.models import Producto
from inicio.models import Empleado
from django.contrib.auth.models import User  

class Reparacion(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()  
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='reparaciones', null=True, blank=True)  

    def __str__(self):
        return f"Reparación {self.id} - {self.descripcion}"

class Estado(models.Model):
    estado_equipo = models.CharField(max_length=100)
    fecha_equipo = models.DateField()  
    descripcion = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='estados', null=True, blank=True)  

    def __str__(self):
        return f"Estado {self.estado_equipo} - {self.producto.nombre if self.producto else 'Desconocido'}"

class Reclamo(models.Model):
    fecha = models.DateField()  
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reclamos')  

    def __str__(self):
        return f"Reclamo {self.id} - {self.descripcion}"

class RespuestaReclamo(models.Model):
    fecha = models.DateField()  
    respuesta = models.CharField(max_length=100)
    reclamo = models.ForeignKey(Reclamo, on_delete=models.CASCADE, related_name='respuestas')  
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='respuestas_reclamo', null=True, blank=True)  

    def __str__(self):
        return f"Respuesta {self.id} - {self.respuesta[:20]}..."
