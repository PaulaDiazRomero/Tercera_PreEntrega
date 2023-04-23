from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50)    
    apellido = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=50)
    email = forms.EmailField()

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)    
    email = forms.EmailField()

class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_de_entrega = forms.DateField()