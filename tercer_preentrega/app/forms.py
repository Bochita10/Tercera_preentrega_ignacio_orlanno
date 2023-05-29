from django import forms

class Arquitecto(forms.Form):
    nombre= forms.CharField(),
    apellido= forms.CharField(),
    email= forms.EmailField()

class Barrio(forms.Form):
    nombre= forms.CharField()