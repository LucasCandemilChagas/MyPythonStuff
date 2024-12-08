from django import forms
from django.core.exceptions import ValidationError
from .models import Aposta

class ApostaForm(forms.ModelForm):
    class Meta:
        model = Aposta
        fields = ['numero1', 'numero2', 'numero3', 'numero4', 'numero5']
        labels = {
            'numero1': 'Número 1',
            'numero2': 'Número 2',
            'numero3': 'Número 3',
            'numero4': 'Número 4',
            'numero5': 'Número 5',
        }

    
    def clean_numero1(self):
        numero = self.cleaned_data['numero1']
        if numero <= 0 or numero > 50:
            raise ValidationError('Invalido!')
        return numero
    
    def clean_numero2(self):
        numero = self.cleaned_data['numero2']
        if numero <= 0 or numero > 50 or str(numero).startswith('0'):
            raise ValidationError('Invalido!')
        return numero
    
    def clean_numero3(self):
        numero = self.cleaned_data['numero3']
        if numero <= 0 or numero > 50 or str(numero).startswith('0'):
            raise ValidationError('Invalido!')
        return numero
    
    def clean_numero4(self):
        numero = self.cleaned_data['numero4']
        if numero <= 0 or numero > 50 or str(numero).startswith('0'):
            raise ValidationError('Invalido!')
        return numero
    
    def clean_numero5(self):
        numero = self.cleaned_data['numero5']
        if numero <= 0 or numero > 50 or str(numero).startswith('0'):
            raise ValidationError('Invalido!')
        return numero
      
class ApostasForm(forms.Form):
    numero_de_apostas = forms.IntegerField(min_value=2, max_value=100)
    