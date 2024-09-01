from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda import views  # Asegúrate de importar las vistas correctamente

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('procesoCompra', views.proceso_compra,name='ProcesoC'),
    path('add-to-cart/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-comment/<int:producto_id>/',views.add_comment, name='add_comment'),
    path('rate-product/<int:producto_id>/',views.rate_product, name='rate_product'),
    # otras URLs...
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
