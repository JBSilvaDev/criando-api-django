from django.http import JsonResponse
from escola.serializer import *
from escola.models import *
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Dados que serão exibidos no JSON
class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos
    """
    # Termo de busca geral
    queryset = Aluno.objects.all()
    # Classe que faz a conversao do JSON
    serializer_class = AlunoSerializer
    # Autenticação
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Exibindo todas as Matriculas
    """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# Classe tipo view, nao é possivel fazer POST, PUT, PATCH, DELET
class ListaMatriculaAlunosView(generics.ListAPIView):
    """
    Listando matriculas de alunos
    """
    # Query de pesquisa por id passado na URL do setup
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculadoEmCursoView(generics.ListAPIView):
    """
    Listando alunos matriculados nos cursos
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaAlunosMatriculadosEmUmCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
