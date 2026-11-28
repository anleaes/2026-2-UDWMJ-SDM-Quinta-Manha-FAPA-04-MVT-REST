from django.db import models

# Create your models here.

class Especialidade(models.Model):
    tipo = models.CharField('tipo', max_length=25)
    prerequisito = models.CharField('prerequisito', max_length=40)
    status = models.CharField('status', max_length=15)

    class Meta:
        verbose_name = 'especialidade'
        verbose_name_plural = 'especialidades'

    def __str__(self):
        return f'{self.tipo}'

    