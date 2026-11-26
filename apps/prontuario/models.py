from django.db import models
from paciente.models import Paciente

# Create your models here.

class Prontuario(models.Model):
    tipo_sanguineo = models.CharField('Sangue', max_length=1)
    alergias = models.CharField('Alergias', max_length=40)
    historico_familiar = models.CharField('Historico Familiar', max_length=40)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prontuario'
        verbose_name_plural = 'Prontuarios'
        ordering = ['id']

def __str__(self):
    return f'{self.paciente} - Tipo Sanguineo:{self.tipo_sanguineo}'

