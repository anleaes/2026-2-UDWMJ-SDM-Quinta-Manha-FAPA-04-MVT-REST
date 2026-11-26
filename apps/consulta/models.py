from django.db import models
from django.utils import timezone
from sala.models import Sala
from paciente.models import Paciente
from profissional_saude.models import Profissional_saude

# Create your models here.

class Consulta(models.Model):
    tipo = models.CharField('tipo', max_length=40)
    horario = models.TimeField(default=timezone.now)
    data = models.DateField(default=timezone.now)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE,default=1)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,default=1)
    profissional_saude = models.ForeignKey(Profissional_saude, on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name = 'consulta'
        verbose_name_plural = 'consultas'
        ordering = ['id']

    def __str__(self):
        return f'{self.tipo} - {self.paciente}'