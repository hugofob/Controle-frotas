from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),

    path(
        'excluir/<int:id>/',
        views.excluir_veiculo,
        name='excluir_veiculo'
    ),

    path(
        'editar/<int:id>/',
        views.editar_veiculo,
        name='editar_veiculo'
    ),
]