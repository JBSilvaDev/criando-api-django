from dataclasses import field
from rest_framework import serializers

from escola.models import *

# Conversor de dados da tabela para JSON
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "rg", "cpf", "data_nascimento"]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasAlunosSerializer(serializers.ModelSerializer):
    # Configura o que sera exibido no value de cada chave do json
    nome = serializers.ReadOnlyField(source="aluno.nome")
    curso = serializers.ReadOnlyField(source="curso.descricao")
    # Configuração para exibir os dados de exibição e nao os dados do db (dados da variavel NIVEL em models)
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["nome", "curso", "periodo"]

    # Função que que tras as informações para variavel periodo
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosEmUmCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source="aluno.nome")
    class Meta:
        model = Matricula
        fields = ["aluno_nome"]
