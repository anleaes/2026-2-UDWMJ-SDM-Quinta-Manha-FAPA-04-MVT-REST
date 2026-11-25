from django.db import models
from django.utils import timezone

# Create your models here.

class Exame(models.Model):
    tipo = models.CharField('tipo', max_length=20)
    status = models.CharField('status', max_length=20)
    data = models.DateField(default=timezone.now)
    obs = models.CharField('obs', max_length=100)
    laudo = models.CharField('laudo', max_length=100)

    class Meta:
        verbose_name = 'exame'
        verbose_name_plural = 'exames'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'

    
