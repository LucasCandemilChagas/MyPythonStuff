from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # Helper Class that add features

from datetime import datetime
# Not Class-Based View
#def menu(request):
#    return render(request, 'menu/tela_inicial.html', {'today':datetime.today()})

class MenuView(TemplateView):
    template_name ='menu/tela_inicial.html'
    extra_context = {'today':datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name ='menu/authorized.html'
    login_url='/admin'
    
# Not Class-Based View 
#@login_required(login_url='/admin')
#def authorized(request):
#    return render(request, 'menu/authorized.html', {})
