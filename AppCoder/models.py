from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada =models.IntegerField()
    def __str__(self):
        return  f" Nombre: {self.nombre} - Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return  f" Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    def __str__(self):
        return  f" Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - profesion: {self.profesion}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega= models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return  f" Nombre: {self.nombre} - Fecha Entrega: {self.fecha_entrega} - entregado: {self.entregado}"

