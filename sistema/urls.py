from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls), # DIOVANNA -> está correto 
    # path('cadastro/', preciso mostrar a página cadastro.html),
    # KARAM: essa url estava duplicada? foi mantida so em portal.urls. ps: não há cadastro.html. foi criada uma view generica
    ]
