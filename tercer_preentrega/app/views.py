from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import Barrio,Arquitecto,Obra

def inicio(request):
    return render(request, "app/inicio.html")

def obras(request):
    return render(request, "app/obras.html")

def arquitectos(request):
    return render(request, "app/arquitectos.html")

def barrios(request):
    return render(request, "app/barrios.html")

def buscar(request):
    if request.GET["barrio"]:
        barrio = request.GET["barrio"]
        obras = Obra.objects.filter(barrio__icontains=barrio)

        return render(request, 'app/inicio.html', {"obras":obras, "barrio":barrio})
    else:
        response = "No ingresaste barrio"

    return HttpResponse(response)