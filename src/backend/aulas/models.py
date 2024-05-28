from django.db import models

# Create your models here.




class carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)


class profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)
    apellido = models.CharField(max_length=128, null=False, blank= False)
    mostrar = models.CharField(max_length=256, null=False, blank= False)


class materia(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)
    cant_alumnos = models.IntegerField(default=5, null=False, blank= False)
    id_carrera = models.ForeignKey(carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(profesor, on_delete=models.CASCADE) 


class aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False, blank= False)
    ubicacion = models.CharField(max_length=128, null=False, blank= False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)