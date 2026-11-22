from django.db import models
from django.utils import timezone

# Create your models here.

class Agendamento(models.Model):
    chamado = models.CharField('chamado', max_length=4)
    horario = models.TimeField(default=timezone.now)
    data = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'

def __str__(self):
    return f'{self.id} - {self.name}'