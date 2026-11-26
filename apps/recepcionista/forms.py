from .models import Recepcionista
from django import forms

class RecepcionistaForm(forms.ModelForm):

    class Meta:
        model = Recepcionista
        exclude = ()