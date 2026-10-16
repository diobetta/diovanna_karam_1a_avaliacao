from django.contrib import admin
from django.urls import path, include
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls), # DIOVANNA -> está correto 
    # path('cadastro/', preciso mostrar a página cadastro.html),
    # KARAM: essa url estava duplicada? foi mantida so em portal.urls. ps: não há cadastro.html. foi criada uma view generica
    
    # DIOVANNA:
    # ERRO ENCONTRADO: as URLs do app portal não estavam incluídas no roteamento principal
    # CORREÇÃO: utilizado include() para encaminhar as rotas para portal.urls
    path('', include('portal.urls')),
    ]
