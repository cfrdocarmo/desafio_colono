from rest_framework import serializers
from atividades.models import Atividade

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'usuario_id', 'titulo', 'date_create', 'descricao']

class ListaAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'usuario', 'titulo', 'date_create']
