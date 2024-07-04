from django.shortcuts import render,redirect
from .models import Persona
from .forms import CrearPersonaFormulario,BuscarPorServicio
from django.views.generic.detail import DetailView

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
        formulario = CrearPersonaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            persona = Persona(  
                                dni = datos.get("dni"),
                                nombre = datos.get("nombre"), 
                                apellido = datos.get("apellido"),
                                # fecha_nac = datos.get("fecha_nac"),
                                nacionalidad =datos.get("nacionalidad"),
                                telefono = datos.get("telefono"),
                                correo = datos.get('correo'),
                                calle = datos.get("calle"),
                                nro = datos.get("nro"),
                                piso = datos.get("piso"),
                                depto = datos.get("depto"),
                                ciudad = datos.get("ciudad"),
                                provincia = datos.get("provincia"),
                                servicio = datos.get("servicio"),
                                matricula = datos.get("matricula"),
                                disponibilidad = datos.get("disponibilidad"),
                                estado = "ACTIVO",
                                avatar_persona = datos.get("avatar_persona")
                              )
            persona.save()
            return redirect('cargadoexitoso') 
    return render(request,'acostacesarapp/cargarnuevo.html', {'formulario':formulario})

    
def listado(request):
    formulariobuscar = BuscarPorServicio()
    if 'servicio' in request.GET:      
        formulariobuscar = BuscarPorServicio(request.GET)
        if formulariobuscar.is_valid():
            personas = Persona.objects.filter(servicio=formulariobuscar.cleaned_data['servicio'])
        else:
            personas = Persona.objects.all()
    else:
        personas = Persona.objects.all()        
    return render(request,'acostacesarapp/listado.html',{'personas':personas, 'formulariobuscar':formulariobuscar})
        
class DetalleProfesional(DetailView):
    model = Persona
    template_name = 'acostacesarapp/detalleprofesional.html'
    