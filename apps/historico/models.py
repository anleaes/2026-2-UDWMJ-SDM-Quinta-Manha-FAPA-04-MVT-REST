from django.db import models

# Create your models here.

class Historico(models.Model):
    evolucao = models.TextField('Evolução', max_length=100)
    tipo = models.CharField('Tipo', max_length=30)
    risco = models.CharField('Risco', max_length=10)

    class Meta:
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'
        ordering = ['id']

def __str__(self):
 return f'{self.id} - {self.name}'