from django.urls import path

from . import views
urlpatterns = [
    path('lista/', views.NotasListView.as_view()),
    #path('', views.list),
    path('nota/<int:pk>', views.NotasDetailView.as_view()),
]
