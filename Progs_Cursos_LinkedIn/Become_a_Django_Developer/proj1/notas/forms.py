from django import forms

from django.core.exceptions import ValidationError

from .models import Nota

import re

#This is the C of the CRUD

# Same as before, but with more habilities
class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-3'})
        }
        labels = {
            'title': 'Titulo do Item',
            'description': 'Conteudo'
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search(r'[^a-zA-Z\s]', title):
            raise ValidationError('We only accpet items that have just letters and spaces!')
        return title