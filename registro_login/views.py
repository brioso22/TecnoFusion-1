from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm  # Asegúrate de tener un formulario de inicio de sesión
from django import forms

def regis_login(request):
    return render(request,'registro_login.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirige a la página de inicio
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
    return render(request, 'account/login.html', {'form': form})


class TestForm(forms.Form):
    name = forms.CharField(label='Your Name')

def test_view(request):
    form = TestForm()
    return render(request, 'donaciones.html', {'form': form})
