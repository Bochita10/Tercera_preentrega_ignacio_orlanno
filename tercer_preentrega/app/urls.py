from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('obras', views.obras, name="Obras"),
    path('arquitectos', views.arquitectos, name="Arquitectos"),
    path('barrios', views.barrios, name="Barrios"),
    path('buscar/', views.buscar),
    path('login/', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('register/', views.register, name='Registro')
]
