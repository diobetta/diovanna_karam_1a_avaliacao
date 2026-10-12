from django.shortcuts import render


def index(request):
    return render(
        request,
        'templates/portal/index.html'
    )

def cadastro(request):
    return render(request, 'cadastro.html')