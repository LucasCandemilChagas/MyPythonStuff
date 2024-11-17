from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotaForm
from .models import Nota

# Create your views here.
class SobreListView(ListView):
    model = Nota
    context_object_name = "sobre"
    template_name = "sobre/sobre.html"
    
class SuporteListView(ListView):
    model = Nota
    context_object_name = "suporte"
    template_name = "suporte/suporte.html"
    
#Not Class-Based View
#def list(request):
#    all_notas = Nota.objects.all()
#    return render(request, 'notas/notas_list.html', {'notas': all_notas})

class ItemDetailView(DetailView):
    model = Nota
    context_object_name = "nota"
    template_name = "sobre/nota_detail.html"

# This is part of the C of CRUD
# LoginRequiredMixin makes sure that just the user logged in can access
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Nota
    template_name = "sobre/nota_edit_create.html"
    success_url = '/sobre'
    form_class = NotaForm
    login_url = "/admin"

# This is part of the U of CRUD
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Nota
    template_name = "sobre/nota_edit_create.html"
    success_url = '/sobre'
    form_class = NotaForm
    login_url = "/admin"
    

# This is part of the D of CRUD
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Nota
    template_name = "sobre/nota_delete.html"
    success_url = '/sobre'
    login_url = "/admin"
    
    
    

#def detail(request, pk):
#    try:
#        nota = Nota.objects.get(pk=pk)
#    except Nota.DoesNotExist:
#        raise Http404("Nota não encontrada")
#    return render(request, 'notas/nota_detail.html', {'nota': nota})