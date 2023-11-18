from django.http import JsonResponse

# Create your views here.

def alunos(request):
  if request.method == 'GET':
    aluno = {
      'id':1,
      'nome':'JB Silva'
    }
    return JsonResponse(aluno)
