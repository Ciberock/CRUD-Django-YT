from django.contrib import admin
from .models import Jogos

@admin.register(Jogos)
class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'ano_lancamento')


