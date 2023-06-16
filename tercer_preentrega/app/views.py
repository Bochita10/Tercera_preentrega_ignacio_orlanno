from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from app.models import Barrio, Arquitecto, Obra
from app.forms import ArquitectoFormulario, BarrioFormulario, ObraFormulario, UserRegisterForm, ObraForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):
    return render(request, "inicio.html")

@login_required
def obra(request):
    return render(request, "obras.html")

@login_required
def arquitecto(request):
    return render(request, "arquitectos.html")

@login_required
def barrio(request):
    return render(request, "barrios.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {username}")
                return redirect("Inicio")
            else:
                messages.error(request, "Error, datos incorrectos")
                return redirect("Inicio")
        else:
            messages.error(request, "Error, formulario incorrecto")
            return redirect("Inicio")
    
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})

@login_required
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

    return render(request, 'resultadosBusquedaObra.html', {"obras": obras, "barrio": barrio, "message": message})

@login_required
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

@login_required
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

@login_required
def obras(request):
    if request.method == 'POST':
        formulario = ObraFormulario(request.POST) 
        if formulario.is_valid():
            data = formulario.cleaned_data
            obra = Obra(descripcion=data['descripcion'], arquitecto_id=data['arquitecto'], barrio_id=data['barrio'], imagen=request.FILES.get('imagen'), start_date=data['fecha_inicio'], finish_date=data['fecha_fin']) 
            obra.save()
            return redirect('Obras')  # Redirect to 'Obras' view
    else: 
        formulario = ObraFormulario()
    
    return render(request, "obras.html", {"formulario": formulario})

    #     print(formulario)
    #     if formulario.is_valid():
    #         data = formulario.cleaned_data
    #         obra = Obra(descripcion=data['descripcion'], arquitecto_id=data['arquitecto'], barrio_id=data['barrio'], imagen=request.FILES.get('imagen'), start_date=data['fecha_inicio'], finish_date=data['fecha_fin']) 
    #         obra.save()
    #         return render(request, "inicio.html")
    # else: 
    #     formulario = ObraFormulario()
    
    # return render(request, "obras.html", {"formulario": formulario})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje":"Usuario Creado :)"})
    else:
        
        form = UserRegisterForm()
    return render(request, "registro.html", {"form":form})