from django.urls import path

from . import views

urlpatterns = [
    path('', views.aposta, name="aposta.selecao"),
    path('mais/', views.apostas, name="mais"),
]
