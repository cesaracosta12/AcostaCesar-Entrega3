from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import FormularioRegistroUsuario ,FormularioEditarPerfil, FormularioCambiarPassword
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosUsuario
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
            
            DatosUsuario.objects.get_or_create(user=user)
            
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

@login_required
def verperfil(request):
    return render(request,"usuarios/perfil.html",{})

login_required
def editarperfil(request):
    formulario_editarperfil = FormularioEditarPerfil(initial={'avatar':request.user.datosusuario.avatar}, instance=request.user)
    
    if request.method == 'POST':
        formulario_editarperfil = FormularioEditarPerfil(request.POST, request.FILES ,instance=request.user)
        if formulario_editarperfil.is_valid():
           
            request.user.datosusuario.avatar = formulario_editarperfil.cleaned_data.get('avatar')
            request.user.datosusuario.save()
            formulario_editarperfil.save()
            return redirect('verperfil')
    
    return render(request,"usuarios/editarperfil.html",{'formulario_editarperfil':formulario_editarperfil})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/editarpassword.html'
    success_url = reverse_lazy('verperfil')
    # form = FormularioCambiarPassword()