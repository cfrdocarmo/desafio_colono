from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import AtividadeForm
from .models import Atividade
from rest_framework import viewsets, generics
from atividades.models import Atividade
from atividades.serializer import AtividadeSerializer, ListaAtividadeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ListaAtividadesUsuarios(generics.ListAPIView):
    def get_queryset(self):
        queryset = Atividade.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAtividadeSerializer


class AtividadeViewSets(viewsets.ModelViewSet):
    """ Exibindo todas as Atividades"""
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


def atividades(request):
    if request.method == 'GET':
        atividade = {'id':1, 'titulo': 'Viagem'}

def atividade_list(request):
    context = {'atividade_list' : Atividade.objects.all()}
    return render(request, "atividades/atividade_list.html", context)

def atividade_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AtividadeForm()
        else:
            atividade = Atividade.objects.get(pk=id)
            form = AtividadeForm(instance=atividade)
        return render(request, 'atividades/atividade_form.html', {'form': form})
    else:
        if id == 0:
            form = AtividadeForm(request.POST)
        else:
            atividade = Atividade.objects.get(pk=id)
            form = AtividadeForm(request.POST, instance= atividade)

        if form.is_valid():
            form.save()
        return redirect('/atividades/list')

def atividade_delete(request, id):
    atividade = Atividade.objects.get(pk=id)
    atividade.delete()
    return redirect('/atividades/list')

def dashboard(request):
    pass