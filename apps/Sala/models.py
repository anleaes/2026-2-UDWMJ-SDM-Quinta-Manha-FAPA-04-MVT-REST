from django.db import models

# Create your models here.

class Sala(models.Model):
    numero = models.CharField('numero', max_length=2)
    status = models.CharField('status',max_length=15)
    setor = models.CharField('setor',max_length=1)

    class Meta:
        verbose_name = 'sala'
        verbose_name_plural = 'salas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'