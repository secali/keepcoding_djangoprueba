from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40, primary_key=True)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(primary_key=True)

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(primary_key=True)
    profesion= models.CharField(max_length=30)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30,primary_key=True)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
