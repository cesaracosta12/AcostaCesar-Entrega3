from django import forms

class CrearPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40,required=True)
    apellido = forms.CharField(max_length=40,required=True)
    dni= forms.IntegerField(required=True)
    edad= forms.IntegerField(required=False)
    correo = forms.EmailField(max_length=20,required=True)
    direccion =  forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=40,required=True)
