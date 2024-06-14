from django.shortcuts import render,redirect
from .models import Persona
from .forms import CrearPersonaFormulario,BuscarPorEspecialidad
# Create your views here.
def inicio(request):  
    if request.user.is_authenticated:
        return render(request,'acostacesarapp/index_user_auth.html')
    else:
        return render(request,'acostacesarapp/index.html')

def contacto(request):
    return render(request,'acostacesarapp/contacto.html')

def cargadoexitoso(request):
    return render(request,'acostacesarapp/cargadoexitoso.html')

def cargarnuevo(request):
    formulario = CrearPersonaFormulario()
    if request.method == 'POST':
        formulario = CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            persona = Persona(nombre = datos.get("nombre"), apellido = datos.get('apellido'),correo = datos.get('correo'),dni = datos.get("dni"),edad = datos.get("edad"),direccion = datos.get("direccion"),especialidad = datos.get("especialidad"),matricula = datos.get("matricula"),telefono = datos.get("telefono"))
            persona.save()
            return redirect('cargadoexitoso') 
    return render(request,'acostacesarapp/cargarnuevo.html', {'formulario':formulario})
    
def listado(request):
    formulariobuscar = BuscarPorEspecialidad(request.GET)
    if formulariobuscar.is_valid():
        personas = Persona.objects.filter(especialidad=formulariobuscar.cleaned_data['especialidad'])
        return render(request,'acostacesarapp/listado.html',{'personas':personas, 'formulariobuscar':formulariobuscar})
    else:
        personas = Persona.objects.all()
        return render(request,'acostacesarapp/listado.html',{'personas':personas, 'formulariobuscar':formulariobuscar})
        



    