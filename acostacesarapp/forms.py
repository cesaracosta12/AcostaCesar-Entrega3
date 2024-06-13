from django import forms


especialidad_opciones= (
    ("OTRO","OTRO"),
    ("GASISTA","GASISTA"),
    ("ELECTRICISTA","ELECTRICISTA"),
    ("PLOMERO","PLOMERO"),
    ("CHOFER","CHOFER"),
    ("SERVICIO TECNICO AIRE ACONDICIONADO","SERVICIO TECNICO AIRE ACONDICIONADO"),
    ("SERVICIO TECNICO LAVARROPAS","SERVICIO TECNICO LAVARROPAS"),
    ("GUARDIA","GUARDIA"),
    ("MECANICO","MECANICO"),
)


class CrearPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40,required=True)
    apellido = forms.CharField(max_length=40,required=True)
    dni= forms.IntegerField(required=True)
    edad= forms.IntegerField()
    correo = forms.EmailField(max_length=40)
    telefono = forms.CharField(max_length=50)
    direccion =  forms.CharField(max_length=50)
    especialidad = forms.ChoiceField(choices=especialidad_opciones )
    matricula = forms.IntegerField(required=True)

class BuscarPorEspecialidad(forms.Form):
    especialidad = forms.ChoiceField(choices=especialidad_opciones)