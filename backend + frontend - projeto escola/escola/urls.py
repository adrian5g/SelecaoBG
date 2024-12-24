from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('editar_nota/<int:id>/', editar_nota, name='editar_nota'),
    path('remover_nota/<int:id>/<int:disciplina_id>/', remover_nota, name='remover_nota'),
    path('cadastrar_nota/<int:id>/<int:disciplina_id>/', cadastrar_nota, name='cadastrar_nota'),
    path('listar_notas/<int:id>/<int:periodo>/', listar_notas, name='listar_notas'),
    path('remover_aluno/<int:id>/', remover_aluno, name='remover_aluno'),
    path('editar_aluno/<int:id>/', editar_aluno, name='editar_aluno'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_alunos/', listar_alunos, name='listar_alunos'),
    path('remover_disciplina/<int:curso_id>/<int:id>', remover_disciplina, name='remover_disciplina'),
    path('cadastrar_disciplina/<int:id>/', cadastrar_disciplina, name='cadastrar_disciplina'),
    path('listar_disciplinas/<int:id>/', listar_disciplinas, name='listar_disciplinas'),
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
    path('remover_curso/<int:id>/', remover_curso, name='remover_curso'),
    path('cadastrar_curso', cadastrar_curso, name='cadastrar_curso'),
    path('listar_cursos', listar_cursos, name='listar_cursos')
]
