from django.db import models

# Create your models here.

class Diagnostico(models.Model):
    descricao = models.TextField('Evolução', max_length=100)

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'

    