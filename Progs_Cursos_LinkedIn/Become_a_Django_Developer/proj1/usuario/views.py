from django.shortcuts import render
from django.contrib.auth.models import User
#from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import Http404


# Create your views here.

def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404("Usuario não encontrado!")
    return render(request, 'usuario_detail.html', {'user': user})