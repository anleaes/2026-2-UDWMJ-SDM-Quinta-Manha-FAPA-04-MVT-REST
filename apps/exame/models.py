from django.db import models
from django.utils import timezone
from consulta.models import Consulta
from paciente.models import Paciente
from profissional_saude.models import Profissional_saude

# Create your models here.

class Exame(models.Model):
    tipo = models.CharField('tipo', max_length=20)
    status = models.CharField('status', max_length=20)
    data = models.DateField(default=timezone.now)
    obs = models.CharField('obs', max_length=100)
    laudo = models.CharField('laudo', max_length=100)
    consulta = models.ForeignKey(Consulta,on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey(Profissional_saude,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'exame'
        verbose_name_plural = 'exames'
        ordering = ['id']

    def __str__(self):
        return f'{self.tipo} - {self.paciente}'

    
