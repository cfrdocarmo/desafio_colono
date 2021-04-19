from django.contrib import admin
from .models import Atividade


class ListandoAtividade(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'date_create', 'descricao', 'usuario_id',)
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'usuario',)
    list_per_page = 5



admin.site.register(Atividade, ListandoAtividade)

