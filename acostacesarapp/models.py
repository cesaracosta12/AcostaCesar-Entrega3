from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni= models.IntegerField()
    edad= models.IntegerField()
    correo = models.CharField(max_length=20)
    direccion =  models.CharField(max_length=50)
    especialidad = models.CharField(max_length=40)
    estado = models.BooleanField(default=True)
    