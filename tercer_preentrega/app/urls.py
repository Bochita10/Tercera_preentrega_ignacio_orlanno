from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('obras', views.obras, name="Obras"),
    path('arquitectos', views.obras, name="Arquitectos"),
    path('barrios', views.obras, name="Barrios"),
    path('buscar/', views.buscar)
]
