from django.shortcuts import render
from django.forms import formset_factory
from .forms import ApostaForm, ApostasForm

# Create your views here.
def aposta(request):
    filled_multform = ApostasForm()
    if request.method == 'POST':
        filled_form = ApostaForm(request.POST)
        nota = ''
        if filled_form.is_valid():
            created_form = filled_form.save()
            created_form_pk = created_form.id
            nota = (f"Aposta {filled_form.cleaned_data['numero1']} "
                    f"{filled_form.cleaned_data['numero2']} "
                    f"{filled_form.cleaned_data['numero3']} "
                    f"{filled_form.cleaned_data['numero4']} "
                    f"{filled_form.cleaned_data['numero5']} enviada com sucesso!")
        else:
            created_form_pk = None
            nota = 'Aposta Invalida! Tente Novamente.'         
        return render(request, 'aposta/aposta.html', {'created_form_pk':created_form_pk,'apostaform':filled_form, 'nota':nota, 'multiplas_apostasform':filled_multform})
    else:
        form = ApostaForm()
    return render(request, 'aposta/aposta.html', {'apostaform':form, 'multiplas_apostasform':filled_multform})

def apostas(request):
    numero_de_apostas = 2
    filled_num_de_apostas = ApostasForm(request.GET)
    if filled_num_de_apostas.is_valid():
        numero_de_apostas = filled_num_de_apostas.cleaned_data['numero_de_apostas']
    ApostaFormSet = formset_factory(ApostaForm, extra=numero_de_apostas)  # type: ignore
    formset = ApostaFormSet()
    if request.method == 'POST':
        filled_formset = ApostaFormSet(request.POST)
        # Verifica se todos foram preenchidos
        not_empty = all( form.changed_data for form in filled_formset )
        if filled_formset.is_valid() and not_empty:
            obs = 'Apostas Criadas!'
        elif not not_empty:
            obs = 'Formulários não foram preenchidos!' 
        else:
            obs = 'Foi(ram) encontrado(s) número(s) inválido(s)!' 
        return render(request, 'aposta/apostas.html', {'obs':obs, 'formset':formset})
    else:
        return render(request, 'aposta/apostas.html', {'formset': formset})           