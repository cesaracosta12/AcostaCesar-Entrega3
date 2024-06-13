from django.shortcuts import render,redirect
from .models import Persona
from .forms import CrearPersonaFormulario
# Create your views here.
def inicio(request):
    return render(request,'acostacesarapp/index.html')

def contacto(request):
    return render(request,'acostacesarapp/contacto.html')

def cargarnuevo(request):
    
    formulario = CrearPersonaFormulario()
    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)
        print(request.POST)
        print('is valid?',formulario.is_valid())
        if formulario.is_valid():
            datos = formulario.cleaned_data
            print('datos: ',datos)
            persona = Persona(nombre = datos.get("nombre"), apellido = datos.get('apellido'),correo = datos.get('correo'),dni = datos.get("dni"),edad = datos.get("edad"),direccion = datos.get("direccion"),especialidad = datos.get("especialidad"))
            persona.save()
            return redirect('listado') 
    return render(request,'acostacesarapp/cargarnuevo.html', {'formulario':formulario})
    
def listado(request):
    return render(request,'acostacesarapp/listado.html')
    