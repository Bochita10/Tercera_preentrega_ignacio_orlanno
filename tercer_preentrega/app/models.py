from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
class Barrio(LoginRequiredMixin, models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Arquitecto(LoginRequiredMixin, models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self) -> str:
        return f"Arq. {self.nombre} {self.apellido}"

class Obra(LoginRequiredMixin, models.Model):
    descripcion=models.CharField(max_length=50)
    arquitecto_id =models.ForeignKey(Arquitecto,on_delete=models.SET_NULL,null=True)
    barrio_id =models.ForeignKey(Barrio,on_delete=models.SET_NULL,null=True)
    imagen = models.ImageField(upload_to='obra_images/', blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return f"Obra {self.descripcion}"

