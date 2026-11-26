from django.db import models
from django.utils import timezone
from consulta.models import Consulta
from prontuario.models import Prontuario

# Create your models here.

class Diagnostico(models.Model):
    descricao = models.TextField('Evolução', max_length=100)
    data = models.DateField(default=timezone.now)
    consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
    prontuario = models.ForeignKey(Prontuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'
        ordering = ['id']

    def __str__(self):
        return f'{self.data}'