from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField('Nombre de la Empresa',max_length=150)
    titularempresa = models.CharField('Titular de la Empresa',max_length=150)
    giro = models.CharField('Giro de la Empresa',max_length=100,blank=True)
    titularproyecto = models.CharField('Titular del Proyecto',max_length=150)
    direccion = models.CharField('Calle y Numero',max_length=255)
    colonia = models.CharField('Colonia',max_length=255)
    codigo_postal =models.CharField('Codigo Postal',max_length=50)
    rfc = models.CharField('RFC', max_length=100, blank=True)
    telefono = models.CharField('Telefono',max_length=50,blank=True)
    email = models.CharField('Email',max_length=100,blank=True)
    social = models.CharField('Redes Sociales',max_length=255,blank=True)

    def __str__(self):
        return self.nombre
