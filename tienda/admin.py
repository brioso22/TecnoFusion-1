from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'descripcion')
    list_filter = ('categoria',)  # Agrega esto si quieres filtrar por categoría en el admin
    search_fields = ('nombre', 'categoria')
