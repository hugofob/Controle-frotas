from django.urls import path
from . import views


urlpatterns = [
    path('', views.motoristas, name='motoristas'),

    path(
        'excluir/<int:id>/',
        views.excluir_motorista,
        name='excluir_motorista'
    ),

    path(
        'editar/<int:id>/',
        views.editar_motorista,
        name='editar_motorista'
    ),
]