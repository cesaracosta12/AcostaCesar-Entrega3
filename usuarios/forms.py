from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {key:'' for key in fields}
    