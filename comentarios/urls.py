from django.urls import path
from . import views

urlpatterns = [
    path('', views.comentarios, name='comentarios'),

path(
        'excluir/<int:id>/',
        views.excluir_comentario,
        name='excluir_comentario'
    ),

    path(
        'editar/<int:id>/',
        views.editar_comentario,
        name='editar_comentario'
    ),
]