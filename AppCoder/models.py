from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada =models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return  self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    def __str__(self):
        return  self.nombre


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_entrega= models.DateField()
    entregado = models.BooleanField()



