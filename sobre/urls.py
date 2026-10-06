from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre, name='sobre'),

    path('manutencao/', views.manutencao, name='manutencao'),
    path('postos/', views.postos, name='postos'),
    path('borracharia/', views.borracharia, name='borracharia'),
    path('oficinas/', views.oficinas, name='oficinas'),
]