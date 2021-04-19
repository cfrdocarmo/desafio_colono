from django.contrib import admin
from .models import Usuario

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    list_display_links = ('id', 'name')
    search_fields = ('nome',)
    list_per_page = 5

admin.site.register(Usuario, ListandoUsuarios)
# Register your models here.
