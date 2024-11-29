from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin # Helper Class that add features
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

from datetime import datetime
# Not Class-Based View
#def menu(request):
#    return render(request, 'menu/tela_inicial.html', {'today':datetime.today()})

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'menu/register.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('menu.principal')
        return super().get(request,*args,**kwargs)

class LogoutInterfaceView(LogoutView):
    template_name ='menu/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'menu/login.html'

class MenuView(TemplateView):
    template_name ='menu/tela_inicial.html'
    extra_context = {'today':datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name ='menu/authorized.html'
    login_url='/admin'
    
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff: # type: ignore
            return redirect('menu.principal')
        return super().get(request,*args,**kwargs)


# Not Class-Based View 
#@login_required(login_url='/admin')
#def authorized(request):
#    return render(request, 'menu/authorized.html', {})
