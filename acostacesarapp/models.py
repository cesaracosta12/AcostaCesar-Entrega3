from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni= models.IntegerField()
    edad= models.IntegerField()
    correo = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=50,default='-')
    direccion =  models.CharField(max_length=50)
    especialidad = models.CharField(max_length=40,null=False,blank=False,error_messages="")
    matricula = models.IntegerField(default=0)

    