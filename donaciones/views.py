from django.shortcuts import render

def donaciones(request):
    return render(request, 'donaciones.html')