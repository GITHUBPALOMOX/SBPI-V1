from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField('Nombre Carrera', max_length=150)    

    def __str__(self):
        return self.nombre