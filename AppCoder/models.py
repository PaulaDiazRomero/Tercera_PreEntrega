from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)    
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
#
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    def __str__(self):
        return f"{self.nombre} - Entregado"