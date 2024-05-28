from django.db import models

# Create your models here.




class Carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)


class Profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)
    apellido = models.CharField(max_length=128, null=False, blank= False)
    mostrar = models.CharField(max_length=256, null=False, blank= False)


class Materia(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank= False)
    cant_alumnos = models.IntegerField(default=5, null=False, blank= False)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE) 


class Aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False, blank= False)
    ubicacion = models.CharField(max_length=128, null=False, blank= False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)


class Reserva_Aula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField() 
    observacion = models.TextField(max_length=256, null=False, blank= False)



class Horario_Materia(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva_Aula, on_delete=models.CASCADE)
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField() 
