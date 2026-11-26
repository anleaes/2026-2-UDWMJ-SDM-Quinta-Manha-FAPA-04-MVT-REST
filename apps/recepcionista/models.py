from django.db import models

# Create your models here.

class Recepcionista(models.Model):
    nome = models.CharField('nome',max_length=40)
    telefone = models.CharField('telefone',max_length=9)
    cpf = models.CharField('cpf',max_length=11)
    turno = models.CharField('turno',max_length=15)

    class Meta:
        verbose_name = 'recepcionista'
        verbose_name_plural = 'recepcionistas'

def __str__(self):
    return f'{self.nome}'
    