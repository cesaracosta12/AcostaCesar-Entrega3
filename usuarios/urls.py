from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('registrar/',views.registro,name='registro'),
    path('perfil/',views.verperfil, name="verperfil"),
    path('perfil/editar/',views.editarperfil, name="editarperfil"),
    path('perfil/editar/password/',views.CambiarPassword.as_view(), name="editarpassword"),
    
]
