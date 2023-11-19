from django.contrib import admin
from escola.models import *


# Register your models here.
# Classes para exibição da tabela na area de ADM
class ListandoAlunos(admin.ModelAdmin):
    # Itens exbidos
    list_display = ("id", "nome", "rg" ,"cpf" ,"data_nascimento",)
    # Itens que podem ser clicados
    list_display_links = ("id", "nome",)
    # Termos de busca
    search_fields = ('nome',)
    # Quantidade por pagina
    list_per_page = 20

admin.site.register(Aluno, ListandoAlunos)


class ListandoCursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ("id", "codigo_curso",)
    search_fields = ('codigo_curso',)

admin.site.register(Curso, ListandoCursos)


class ListandoMatriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ("id", "aluno",)

admin.site.register(Matricula, ListandoMatriculas)

