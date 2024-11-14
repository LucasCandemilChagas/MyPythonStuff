from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Nota

# Create your views here.

class NotasListView(ListView):
    model = Nota
    context_object_name = "notas"
    template_name = "notas/notas_list.html"
    
#Not Class-Based View
#def list(request):
#    all_notas = Nota.objects.all()
#    return render(request, 'notas/notas_list.html', {'notas': all_notas})

class NotasDetailView(DetailView):
    model = Nota
    context_object_name = "nota"
    template_name = "notas/nota_detail.html"
    


#def detail(request, pk):
#    try:
#        nota = Nota.objects.get(pk=pk)
#    except Nota.DoesNotExist:
#        raise Http404("Nota não encontrada")
#    return render(request, 'notas/nota_detail.html', {'nota': nota})