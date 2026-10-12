from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # DIOVANNA -> está correto 
    # path('cadastro/', preciso mostrar a página cadastro.html),
    # DIOVANNA 
    # ERRO ENCONTRADO: havia texto em linguagem natural dentro do path, causando SyntaxError
    # CORREÇÃO: removida a rota duplicada de cadastro e utilizado include() para chamar as URLs do app portal
    path('', include('portal.urls')),
]
