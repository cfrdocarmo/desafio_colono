from django import forms
from atividades.models import Atividade



class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ('usuario','titulo', 'descricao', 'date_create')
        labels = {
            'usuario':'Usuário',
            'titulo' : 'Titulo',
            'descricao' : 'Descrição',
            'date_create' : 'Data Criação'

        }




