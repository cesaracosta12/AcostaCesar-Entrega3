from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import FormularioRegistroUsuario
# Create your views here.

def login(request):
    formulario_login = AuthenticationForm()
    
    if request.method == "POST":
        formulario_login = AuthenticationForm(request,data=request.POST)
        if formulario_login.is_valid():
            usuario = formulario_login.cleaned_data.get('username')
            contraseña = formulario_login.cleaned_data.get('password')
            
            user = authenticate(request, username= usuario, password= contraseña)
            django_login(request,user)
            
            return redirect('inicio')
        
    return render(request, 'usuarios/login.html',{'formulario_login':formulario_login})
            
    
def registro(request):
    formulario_registro = FormularioRegistroUsuario()
    
    if request.method == 'POST':
        formulario_registro = FormularioRegistroUsuario(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect('login')
                            
    return render(request,'usuarios/registro.html',{'formulario_registro':formulario_registro})