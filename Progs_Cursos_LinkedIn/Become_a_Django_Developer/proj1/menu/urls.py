from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuView.as_view()),
    path('restricted_menu/', views.AuthorizedView.as_view()),
]