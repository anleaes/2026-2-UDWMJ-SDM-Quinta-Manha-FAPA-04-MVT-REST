from django.db import models
from prontuario.models import Prontuario


# Create your models here.

class Historico(models.Model):
    evolucao = models.TextField('Evolução', max_length=100)
    tipo = models.CharField('Tipo', max_length=30)
    risco = models.CharField('Risco', max_length=10)
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'
        ordering = ['id']

    def __str__(self):
     return f'{self.risco}'