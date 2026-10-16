from django import forms

# DIOVANNA:
# ERRO ENCONTRADO: o model Professor estava sendo importado sem indicar aonde ele está localizado
# CORREÇÃO: alterado o import para buscar Professor em portal.models
from portal.models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
