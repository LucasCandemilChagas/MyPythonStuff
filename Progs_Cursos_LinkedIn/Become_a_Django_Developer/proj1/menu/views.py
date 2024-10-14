from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import datetime

def menu(request):
    return render(request, 'menu/tela_inicial.html', {'today':datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'menu/authorized.html', {})
