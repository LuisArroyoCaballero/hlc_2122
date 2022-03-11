from django.db import models
from ast import Str

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre completo del Cliente')
    direccion=models.CharField(max_length=150)
    email=models.CharField(max_length=50)
    telefono=models.CharField(max_length=12)
    def __str__(self):
        return "nombre: "+ self.nombre+" dirección: "+ self.direccion+" email: "+self.email+"telefono: "+ self.telefono 


class Articulos(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return 'El nombre es {} y su precio es {}'.format(self.nombre, self.precio)


class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return "numero: "+ self.numero+" fecha: "+ self.fecha+" entregado: "+self.entregado