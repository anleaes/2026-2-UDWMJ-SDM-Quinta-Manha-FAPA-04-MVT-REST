from django.db import models
from django.utils import timezone

# Create your models here.

class Plano_saude(models.Model):
    nome = models.CharField('nome', max_length=30)
    numero = models.CharField('numero', max_length=20)
    validade = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'plano_saude'
        verbose_name_plural = 'planos_saude'
        ordering = ['id']

    def __str__(self):
        return  f'{self.id} - {self.name}'