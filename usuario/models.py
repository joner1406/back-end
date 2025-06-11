from django.db import models
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)  

    def __str__(self):
        return str(self.nombre)
    

class CientificoDeDatos(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)  

    def __str__(self):
        return str(self.nombre)



class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)  

    def __str__(self):
        return str(self.nombre)
    

class Cultivo(models.Model):
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    fecha_siembra = models.DateField()

    def __str__(self):
        return str(self.tipo) 
    
class DatoClimatico(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    lluvia = models.FloatField()
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='datos_climaticos')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.temperatura)
    

class ModeloPredictivo(models.Model):
    nombre_modelo = models.CharField(max_length=100)
    fecha_entrenamiento = models.DateField()
    cultivo = models.ForeignKey
    