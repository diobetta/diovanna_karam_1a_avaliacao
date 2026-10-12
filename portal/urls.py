from django.urls import path
from portal import views

urlpatterns = [
    path('index/', views.index),
    # path('cadastro/', views.cadastro),
    # ERRO ENCONTRADO: não havia view cadastrada para o cadastro. view foi incluida. 
    path('cadastro/', views.cadastro, name ='cadastro' )

]
