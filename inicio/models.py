from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, related_name='empleados')
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE, related_name='empleados', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelos')

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre