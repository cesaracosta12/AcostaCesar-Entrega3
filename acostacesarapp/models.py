from django.db import models
from datetime import date

# Create your models here.
class Persona(models.Model):
    # informacion personal
    dni= models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nac= models.DateField(null=True, blank=True) 
    nacionalidad = models.CharField(max_length=40,null=False,blank=False,error_messages="")
    
    # avatar
    avatar_persona = models.ImageField(upload_to='avatares',blank=True,null=True)
    
    # informacion de contacto
    telefono = models.CharField(max_length=50,default='-')
    correo = models.EmailField(max_length=40)
    
    # direccion
    calle =  models.CharField(max_length=50,null=False,blank=False)
    nro = models.IntegerField()
    piso = models.CharField(max_length=50)
    depto = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    
    # informacion laboral
    servicio = models.CharField(max_length=40,null=False,blank=False,error_messages="")
    matricula = models.IntegerField(default=0)
    # agregar en el formulario las choices
    disponibilidad = models.CharField(max_length=40,null=False,blank=False,error_messages="")

    # informacion no visible por ahora
    estado = models.CharField(max_length=50,default='ACTIVO')
    
    def edad(self):
        if self.fecha_nac:
            hoy = date.today()
            return hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))
        return None