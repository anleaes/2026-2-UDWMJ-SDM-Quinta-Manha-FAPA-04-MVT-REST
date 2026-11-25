from django import forms
from .models import Historico

class HistoricoForm(forms.ModelForm):

  class Meta:
    model = Historico
    exclude = ()