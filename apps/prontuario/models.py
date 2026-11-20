from django.db import models

# Create your models here.

class Prontuario(models.Model):
    tipo_sanguineo = models.CharField('Sangue', max_length=1)
    alergias = models.CharField('Alergias', max_length=40)
    historico_familiar = models.CharField('Historico Familiar', max_length=40)

    class Meta:
        verbose_name = 'Prontuario'
        verbose_name_plural = 'Prontuarios'
        ordering = ['id']

def __str__(self):
    return f'{self.id} - {self.name}'

