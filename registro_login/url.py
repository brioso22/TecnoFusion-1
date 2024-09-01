from django.urls import path
from . import views

urlpatterns =[
    path('', views.regis_login, name='ingresar'),
    path('login/',views.login_view, name='login'),
]