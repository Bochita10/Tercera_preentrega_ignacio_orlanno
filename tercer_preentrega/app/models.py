from django.db import models

# Create your models here.
class Barrio(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Arquitecto(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self) -> str:
        return f"Arq. {self.nombre} {self.apellido}"

class Obra(models.Model):
    descripcion=models.CharField(max_length=50)
    arquitecto_id =models.ForeignKey(Arquitecto,on_delete=models.SET_NULL,null=True)
    barrio_id =models.ForeignKey(Barrio,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"Obra {self.descripcion}"

