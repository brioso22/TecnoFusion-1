from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Comentarios, CalificacionProducto
from django.contrib import messages

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def proceso_compra(request):
    return render(request, 'proceso_compra.html')


@login_required
def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Aquí puedes añadir el producto al carrito del usuario.
    # Ejemplo: agregar producto a la sesión o a un modelo de carrito
    messages.success(request, f'Producto "{producto.nombre}" agregado al carrito.')
    return redirect('tienda')

@login_required
def add_comment(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Aquí puedes manejar la adición de comentarios.
    # Por ejemplo, puedes usar un formulario para recibir y guardar comentarios.
    messages.success(request, f'Comentario añadido al producto "{producto.nombre}".')
    return redirect('tienda')

@login_required
def rate_product(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Aquí puedes manejar la calificación del producto.
    # Por ejemplo, puedes usar un formulario para recibir y guardar calificaciones.
    messages.success(request, f'Calificación añadida al producto "{producto.nombre}".')
    return redirect('tienda')