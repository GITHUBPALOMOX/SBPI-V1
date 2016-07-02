from django.db import models
from django.utils import timezone
from apps.empresas.models import Empresa

TIPO_PROYECTO_CHOICES = (
    ('I', 'Interno'),
    ('E', 'Externo'),
)
ESTADO_PROYECTO_CHOICES = (
    ('SI','asignado'),
    ('NO','no asignado'),

    )

# modelo proyecto
class Proyecto(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='proyectos')
    nombre = models.CharField('Nombre proyecto',max_length=150)
    tipo_proyecto= models.CharField('Proyecto: INTERNO o EXTERNO',max_length=1,choices=TIPO_PROYECTO_CHOICES)
    descripcion = models.CharField('Descripcion del proyecto',max_length=255,blank=True)
    estado = models.CharField('Proyecto: Asignado o NO Asignado',max_length=10,choices=ESTADO_PROYECTO_CHOICES)
    matricula = models.CharField('Matricula Asignada',max_length=10)
    archivo = models.FileField('subir archivo',upload_to='blog/archivos', blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre

    def publish(self):
        self.publish_date = timezone.now()
        self.save()