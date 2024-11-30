from django.shortcuts import render
from .forms import ApostaForm

# Create your views here.
def aposta(request):
    if request.method == 'POST':
        filled_form = ApostaForm(request.POST)
        if filled_form.is_valid():
            nota = (f"Aposta {filled_form.cleaned_data['numero1']} "
                    f"{filled_form.cleaned_data['numero2']} "
                    f"{filled_form.cleaned_data['numero3']} "
                    f"{filled_form.cleaned_data['numero4']} "
                    f"{filled_form.cleaned_data['numero5']} enviada com sucesso!")
            new_form = ApostaForm()
            return render(request, 'aposta/aposta.html', {'apostaform':new_form, 'nota':nota})
    else:
        filled_form = ApostaForm()
    return render(request, 'aposta/aposta.html', {'apostaform':filled_form})