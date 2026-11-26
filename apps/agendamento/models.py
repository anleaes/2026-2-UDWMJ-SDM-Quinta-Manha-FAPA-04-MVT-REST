from django.db import models
from django.utils import timezone
from profissional_saude.models import Profissional_saude
from paciente.models import Paciente
from recepcionista.models import Recepcionista

# Create your models here.

class Agendamento(models.Model):
    chamado = models.CharField('chamado', max_length=4)
    horario = models.TimeField(default=timezone.now)
    data = models.DateField(default=timezone.now)
    profissional_saude = models.ForeignKey(Profissional_saude, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    recepcionista = models.ForeignKey(Recepcionista, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'

def __str__(self):
    return f'{self.id} - {self.name}'