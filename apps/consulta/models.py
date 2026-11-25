from django.db import models
from django.utils import timezone

# Create your models here.

class Consulta(models.Model):
    tipo = models.CharField('tipo', max_length=40)
    horario = models.TimeField(default=timezone.now)
    data = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'consulta'
        verbose_name_plural = 'consultas'