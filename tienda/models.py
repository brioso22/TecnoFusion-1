from django.db import models
from django.contrib.auth.models import User  # Utilizando el modelo de usuario por defecto de Django

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    

class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')  
    fecha = models.DateTimeField(auto_now_add=True)  
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    productos = models.ManyToManyField(Producto, through='DetalleVenta', related_name='ventas')
    transferencia = models.OneToOneField('Transferencia', on_delete=models.CASCADE, null=True, blank=True, related_name='venta')  

    def __str__(self):
        return f"Venta {self.id} por {self.usuario.username}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField()  
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)  
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en venta {self.venta.id}"

class Transferencia(models.Model):
    metodo_pago = models.CharField(max_length=50)  
    numero_transaccion = models.CharField(max_length=100, unique=True)  
    fecha_transaccion = models.DateTimeField()  
    estado = models.CharField(max_length=50)  
    
    def __str__(self):
        return f"Transferencia {self.numero_transaccion}"
    

class ProductosGuardados(models.Model):
    descripcion = models.CharField(max_length=100)
    cantidad_stock = models.IntegerField()
    fecha_guardado = models.DateField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class CalificacionProducto(models.Model):
    calificacion = models.IntegerField()
    comentario_opcional = models.TextField(blank=True, null=True)
    fecha_calificacion = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentarios(models.Model):
    comentario = models.CharField(max_length=800)
    fecha_comentario = models.DateField()
    editado = models.BooleanField(default=False)
    calificacion_producto = models.ForeignKey(CalificacionProducto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respuesta_a_comentario = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
