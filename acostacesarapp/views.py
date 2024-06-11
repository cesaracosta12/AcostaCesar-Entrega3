from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'acostacesarapp/index.html')

def contacto(request):
    return render(request,'acostacesarapp/contacto.html')

def cargarnuevo(request):
    return render(request,'acostacesarapp/cargarnuevo.html')
    
def listado(request):
    return render(request,'acostacesarapp/listado.html')
    