from django.shortcuts import render


def index(request):
    return render(
        request,
        # DIOVANNA:
        # ERRO ENCONTRADO: o caminho do template estava duplicado para "templates"
        # CORREÇÃO: ajustado
        'portal/index.html'
    )

def cadastro(request):
    return render(request, 'cadastro.html') # karam