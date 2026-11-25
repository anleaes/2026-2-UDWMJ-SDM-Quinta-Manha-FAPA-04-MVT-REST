from django import forms
from .models import Profissional_saude

class Profissional_saudeForms(forms.ModelForm):

    class Meta:
        model = Profissional_saude
        exclude = ()