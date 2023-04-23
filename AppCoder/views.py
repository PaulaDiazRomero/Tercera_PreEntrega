from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def inicioApp(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
           curso = Curso()
           curso.nombre = form.cleaned_data['nombre']
           curso.comision = form.cleaned_data['comision']
           curso.save()
           form = CursoForm()
    else:
        form = CursoForm()
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"cursos": cursos, "form": form})    

def profesores(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
           profesor = Profesor()
           profesor.nombre = form.cleaned_data['nombre']
           profesor.apellido = form.cleaned_data['apellido']
           profesor.profesion = form.cleaned_data['profesion']
           profesor.email = form.cleaned_data['email']
           profesor.save()
           form = ProfesorForm()
    else:
        form = ProfesorForm()
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores, "form": form})    

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
           estudiante = Estudiante()
           estudiante.nombre = form.cleaned_data['nombre']
           estudiante.apellido = form.cleaned_data['apellido']
           estudiante.email = form.cleaned_data['email']
           estudiante.save()
           form = EstudianteForm()
    else:
        form = EstudianteForm()
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"estudiantes": estudiantes, "form": form})

def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
           entregable = Entregable()
           entregable.nombre = form.cleaned_data['nombre']
           entregable.fecha_de_entrega = form.cleaned_data['fecha_de_entrega']
           entregable.save()
           form = EntregableForm()
    else:
        form = EntregableForm()
    entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {"entregables": entregables, "form": form})

def busquedaComision(request):
  return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    comision = request.GET["comision"]
    if comision!="":
        cursos = Curso.objects.filter(comision__icontains = comision)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Por favor ingresar una comisión."})