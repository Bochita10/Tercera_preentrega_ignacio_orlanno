from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import Barrio, Arquitecto, Obra
from app.forms import ArquitectoFormulario, BarrioFormulario, ObraFormulario

def inicio(request):
    return render(request, "inicio.html")

def obra(request):
    return render(request, "obras.html")

def arquitecto(request):
    return render(request, "arquitectos.html")

def barrio(request):
    return render(request, "barrios.html")

def buscar(request):
    barrio = request.GET.get("barrio")
    message = None
    obras = None

    if barrio:
        barrioBD = Barrio.objects.filter(nombre__icontains=barrio)
        if barrioBD.exists():
            obras = Obra.objects.filter(barrio_id=barrioBD.first().id)
            message = f"Buscando la obra '{barrio}'"
        else:
            message = "No se encontraron obras en el barrio especificado."
    else:
        message = "No ingresaste barrio."

    return render(request, 'inicio.html', {"obras": obras, "barrio": barrio, "message": message})

def arquitectos(request):
    if request.method == 'POST':
        formulario = ArquitectoFormulario(request.POST) 
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            arquitecto = Arquitecto(nombre=data['nombre'], apellido=data['apellido'], email=data['email']) 
            arquitecto.save()
            return render(request, "inicio.html")
    else: 
        formulario = ArquitectoFormulario()
    
    return render(request, "arquitectos.html", {"formulario": formulario})

def barrios(request):
    if request.method == 'POST':
        formulario = BarrioFormulario(request.POST) 
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            barrio = Barrio(nombre=data['nombre']) 
            barrio.save()
            return render(request, "inicio.html")
    else: 
        formulario = BarrioFormulario()
    
    return render(request, "barrios.html", {"formulario": formulario})

def obras(request):
    if request.method == 'POST':
        formulario = ObraFormulario(request.POST) 
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            obra = Obra(descripcion=data['descripcion'], arquitecto_id=data['arquitecto'], barrio_id=data['barrio']) 
            obra.save()
            return render(request, "inicio.html")
    else: 
        formulario = ObraFormulario()
    
    return render(request, "obras.html", {"formulario": formulario})
