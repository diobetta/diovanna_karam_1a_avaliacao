from django.urls import path
from portal import views

urlpatterns = [
    path('index/', views.index),
    # path('cadastro/', views.cadastro),
    # DIOVANNA
    # ERRO ENCONTRADO: a roda cadastro chamava views.cadastro, mas essa view não existe em views.py
    # CORREÇÃO: removida a rota de cadastro, pois não existe uma view correspondente no projeto
]
