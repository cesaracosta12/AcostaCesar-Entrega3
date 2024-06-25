from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class FormularioRegistroUsuario(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario",max_length=50)
    first_name = forms.CharField(label="Nombre",max_length=50)
    last_name = forms.CharField(label="Apellido",max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {key:'' for key in fields}


class FormularioEditarPerfil(UserChangeForm):
    first_name = forms.CharField(label="Nombre",max_length=50)
    last_name = forms.CharField(label="Apellido",max_length=50)
    email = forms.EmailField()
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','avatar']
        

class FormularioCambiarPassword(PasswordChangeForm):

    password1 = forms.CharField(label='Nueva Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Nueva Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['password1','password2']
        help_texts = {key:'' for key in fields}
    