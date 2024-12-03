from django.db import models

class Project(models.Model):
    nombre_proyecto = models.CharField(max_length=200)
    rut = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)