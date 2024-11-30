from django import forms
from django.core.exceptions import ValidationError
from .models import Aposta

import re
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
        numero1 = self.cleaned_data['numero1']
        if numero1 <= 0 or numero1 > 50 or str(numero1).startswith('0'):
            raise ValidationError('Invalido!')
        return numero1
    
    def clean_numero2(self):
        numero2 = self.cleaned_data['numero2']
        if numero2 <= 0 or numero2 > 50 or str(numero2).startswith('0'):
            raise ValidationError('Invalido!')
        return numero2
    
    def clean_numero3(self):
        numero3 = self.cleaned_data['numero3']
        if numero3 <= 0 or numero3 > 50 or str(numero3).startswith('0'):
            raise ValidationError('Invalido!')
        return numero3
    
    def clean_numero4(self):
        numero4 = self.cleaned_data['numero4']
        if numero4 <= 0 or numero4 > 50 or str(numero4).startswith('0'):
            raise ValidationError('Invalido!')
        return numero4
    
    def clean_numero5(self):
        numero5 = self.cleaned_data['numero5']
        if numero5 <= 0 or numero5 > 50 or str(numero5).startswith('0'):
            raise ValidationError('Invalido!')
        return numero5
    
    
    
    