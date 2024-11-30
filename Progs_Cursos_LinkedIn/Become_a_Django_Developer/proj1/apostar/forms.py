from django import forms

class ApostaForm(forms.Form):
    numero1 = forms.IntegerField(label='Numero 1')
    numero2 = forms.IntegerField(label='Numero 2')
    numero3 = forms.IntegerField(label='Numero 3')
    numero4 = forms.IntegerField(label='Numero 4')
    numero5 = forms.IntegerField(label='Numero 5')
    
    #def clean_numbers(self):
    #    num1 = self.cleaned_data['numero1']
    #    num2 = self.cleaned_data['numero2']
    #    num3 = self.cleaned_data['numero3']
    #    num4 = self.cleaned_data['numero4']
    #    num5 = self.cleaned_data['numero5']
    #    if re.search(r'[^a-zA-Z\s]', num1):
    #        raise ValidationError('We only accpet items that have just letters and spaces!')
    #    return title