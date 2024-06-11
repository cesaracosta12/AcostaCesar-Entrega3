from django.urls import path
from acostacesarapp import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('contacto', views.contacto, name="contacto"),
    path('nuevo', views.cargarnuevo, name="cargarnuevo"),
    path('listado',views.listado, name="listado"),
    
]