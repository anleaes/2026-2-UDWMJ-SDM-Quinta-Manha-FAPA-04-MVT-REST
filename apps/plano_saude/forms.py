from django import forms
from .models import Plano_saude

class Plano_saudeForm(forms.ModelForm):

    class Meta:
        model = Plano_saude
        exclude = ()