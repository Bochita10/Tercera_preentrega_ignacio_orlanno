from django import forms
from app.models import Barrio, Arquitecto

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