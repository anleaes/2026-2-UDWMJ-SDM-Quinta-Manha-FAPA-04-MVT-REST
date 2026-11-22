from django.db import models
from django.utils import timezone

# Create your models here.

class Profissional_saude(models.Model):
     nome = models.CharField('nome', max_length = 40)
     cpf = models.CharField('CPF', max_length = 11)
     telefone = models.CharField('telefone', max_length = 9)
     data = models.DateField(default=timezone.now)

     class Meta:
          verbose_name = 'profissional_saude'
          verbose_name_plural = 'profissionais_saude'

     def __str__(self):
        return f'{self.id} - {self.name}'