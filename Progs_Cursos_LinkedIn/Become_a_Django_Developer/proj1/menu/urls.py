from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuView.as_view(), name="menu.principal"),
    path('restricted_menu/', views.AuthorizedView.as_view(), name="restricted.area"),
]