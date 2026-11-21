from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField('nome', max_length=40)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('telefone', max_length = 9)
    endereco = models.CharField('endereco', max_length= 40)

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.name}'


