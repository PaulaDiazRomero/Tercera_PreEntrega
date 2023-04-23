from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicioApp, name = "inicioApp"),
    path('cursos/', cursos, name = "cursos"),
    path('profesores/', profesores, name = "profesores"),
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('entregables/', entregables, name = "entregables"),
    path('busquedaComision/', busquedaComision, name = "busquedaComision"),
    path('buscar/', buscar, name = "buscar"),
]
