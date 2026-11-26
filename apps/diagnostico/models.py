from django.db import models
from django.utils import timezone

# Create your models here.

class Diagnostico(models.Model):
    descricao = models.TextField('Evolução', max_length=100)
    data = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'