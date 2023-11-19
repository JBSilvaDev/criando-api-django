"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from escola.views import *

# Configura rotas para exibição do JSON
router = routers.DefaultRouter()
# Prefixo, Classe exibição da view, Nome da base (classe model)
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matricula", MatriculaViewSet, basename="Matricula")

urlpatterns = [
    path("admin/", admin.site.urls),
    # Inclui as rotas determinadas em router
    path("", include(router.urls)),
    # Rota com parametro a ser enviado para classe de view, configura para a classe ser apenas de visualização
    path("aluno/<int:pk>/matriculas/", ListaMatriculaAlunosView.as_view()),
    path("curso/<int:pk>/matriculas/", ListaAlunosMatriculadoEmCursoView.as_view()),
]
