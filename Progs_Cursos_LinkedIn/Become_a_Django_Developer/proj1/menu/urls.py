from django.urls import path

from . import views
from usuario import views as u_view

urlpatterns = [
    path('', views.MenuView.as_view(), name="menu.principal"),
    path('restricted_menu/', views.AuthorizedView.as_view(), name="restricted.area"),
    path('login/', views.LoginInterfaceView.as_view(), name="login.area"),
    path('logout/', views.LogoutInterfaceView.as_view(), name="logout.area"),
    path('signup/', views.SignupView.as_view(), name="signup.area"),
]