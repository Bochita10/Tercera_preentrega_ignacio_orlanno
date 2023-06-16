from django import forms
from app.models import Barrio, Arquitecto, Obra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArquitectoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()

class BarrioFormulario(forms.Form):
    nombre= forms.CharField()

class ObraFormulario(forms.Form):
    descripcion = forms.CharField(max_length=50)
    arquitecto = forms.ModelChoiceField(queryset=Arquitecto.objects.all())
    barrio = forms.ModelChoiceField(queryset=Barrio.objects.all())
    imagen = forms.ImageField(required=False)
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2']
        #Saca los mensajes de ayuda
        help_texts = {k:'' for k in fields}

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'finish_date': forms.DateInput(attrs={'type': 'date'}),
        }
