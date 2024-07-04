from django import forms


servicio_opciones= (
    ("OTRO","OTRO"),
    ("ALBAÑIL","ALBAÑIL"),
    ("CARPINTERO","CARPINTERO"),
    ("CERAMISTA","CERAMISTA"),
    ("CHOFER","CHOFER"),
    ("ELECTRICISTA","ELECTRICISTA"),
    ("FLETERO","FLETERO"),
    ("GASISTA","GASISTA"),
    ("GUARDIA","GUARDIA"),
    ("HERRERO","HERRERO"),
    ("JARDINERO","JARDINERO"),
    ("LIMPIAVIDRIOS","LIMPIAVIDRIOS"),
    ("MECANICO","MECANICO"),
    ("PARRILLERO","PARRILLERO"),
    ("PASTELERO","PASTELERO"),
    ("PINTOR","PINTOR"),
    ("PLOMERO","PLOMERO"),
    ("RELOJERO","RELOJERO"),
    ("SERVICIO DE LIMPIEZA","SERVICIO DE LIMPIEZA"),
    ("SERVICIO TECNICO AIRE ACONDICIONADO","SERVICIO TECNICO AIRE ACONDICIONADO"),
    ("SERVICIO TECNICO HELADERA","SERVICIO TECNICO HELADERA"),
    ("SERVICIO TECNICO LAVARROPA","SERVICIO TECNICO LAVARROPA"),
    ("SOLDADOR","SOLDADOR"),
    ("TAPIZADOR","TAPIZADOR"),
    ("TECNICO DE COMPUTADORAS","TECNICO DE COMPUTADORAS"),
)

nacionalidad_opciones =(
    ("ARGENTINA","ARGENTINA"),
    ("BOLIVIA","BOLIVIA"),
    ("BRASIL","BRASIL"),
    ("CHILE","CHILE"),
    ("COLOMBIA","COLOMBIA"),
    ("ECUADOR","ECUADOR"),
    ("PARAGUAY","PARAGUAY"),
    ("URUGUAY","URUGUAY"),
    ("VENEZUELA","VENEZUELA"),
    ("OTRO","OTRO"),
)

disponibilidad_opciones = (
    ("TURNO MAÑANA","TURNO MAÑANA"),
    ("TURNO TARDE","TURNO TARDE"),
    ("FULL TIME","FULL TIME"),
    
)

class CrearPersonaFormulario(forms.Form):
    # informacion personal
    dni= forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=40,required=True)
    apellido = forms.CharField(max_length=40,required=True)
    # fecha_nac = forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y'])
    nacionalidad = forms.ChoiceField(choices=nacionalidad_opciones,required=True)   
    
    # informacion de contacto
    telefono = forms.CharField(max_length=50,required=True)
    correo = forms.EmailField(max_length=40,required=True)
    # direccion
    calle =  forms.CharField(max_length=50,required=True)
    nro = forms.IntegerField(required=True)
    piso = forms.CharField(required=False)
    depto = forms.CharField(max_length=50,required=False)
    ciudad = forms.CharField(max_length=50,required=True)
    provincia = forms.CharField(max_length=50,required=True)
    
    # informacion laboral
    servicio = forms.ChoiceField(choices=servicio_opciones)
    matricula = forms.IntegerField(required=True)
    disponibilidad = forms.ChoiceField(choices=disponibilidad_opciones)
    
    # avatar
    avatar_persona = forms.ImageField(required=True)

class BuscarPorServicio(forms.Form):
    servicio = forms.ChoiceField(choices=servicio_opciones,required=False)