from django.urls import path

from . import views
urlpatterns = [
    path('', views.SobreListView.as_view(), name="sobre.lista"),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name="item.info"),
    path('item/<int:pk>/editar', views.ItemUpdateView.as_view(), name="item.editar"),
    path('item/<int:pk>/deletar', views.ItemDeleteView.as_view(), name="item.deletar"),
    path('item/novo', views.ItemCreateView.as_view(), name="item.novo"),
    path('suporte/', views.SuporteListView.as_view(), name="suporte.lista"),
]

