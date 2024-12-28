from django.shortcuts import render, redirect
from core.models import Curso, Disciplina, Aluno, Nota
from .forms import CursoForm, DisciplinaForm, AlunoForm, NotaForm


def home(request):
    cursos = Curso.objects.count()
    disciplinas = Disciplina.objects.count()
    alunos = Aluno.objects.count()

    context = {
        'quantidade_cursos': cursos,
        'quantidade_disciplinas': disciplinas,
        'quantidade_alunos': alunos
    }

    return render(request, 'index.html', context)


def listar_cursos(request):
    cursos = Curso.objects.all()

    context = {
        'cursos': cursos
    }

    return render(request, 'cursos/listar_cursos.html', context)


def cadastrar_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    context = {
        'form': form
    }

    return render(request, 'cursos/cadastrar_curso.html', context)


def editar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)

    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    context = {
        'form': form
    }

    return render(request, 'cursos/cadastrar_curso.html', context)


def remover_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()

    return redirect('listar_cursos')


def listar_disciplinas(request, id):
    disciplinas = Disciplina.objects.filter(curso=id)

    context = {
        'curso_id': id,
        'disciplinas': disciplinas
    }

    return render(request, 'cursos/listar_disciplinas.html', context)


def cadastrar_disciplina(request, id):
    curso = Curso.objects.get(pk=id)
    form = DisciplinaForm(request.POST or None, curso_default=curso)

    if form.is_valid():
        form.save()
        return redirect('listar_disciplinas', id)

    context = {
        'id': id,
        'form': form
    }

    return render(request, 'cursos/cadastrar_disciplina.html', context)


def remover_disciplina(request, curso_id, id):
    curso = Disciplina.objects.get(pk=id)
    curso.delete()

    return redirect('listar_disciplinas', curso_id)


def listar_alunos(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos
    }

    return render(request, 'alunos/listar_alunos.html', context)


def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_alunos')

    context = {
        'form': form
    }

    return render(request, 'alunos/cadastrar_aluno.html', context)


def editar_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('listar_alunos')

    context = {
        'form': form
    }

    return render(request, 'alunos/cadastrar_aluno.html', context)


def remover_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()

    return redirect('listar_alunos')


def listar_notas(request, id, periodo):
    aluno = Aluno.objects.get(pk=id)
    notas = Nota.objects.filter(aluno=aluno)

    periodos_ate_o_atual = [i for i in range(1, aluno.periodo_atual + 1)]
    disciplinas_periodo_selecionado = Disciplina.objects.filter(
        curso=aluno.curso, periodo_requerido=periodo)

    notas_periodo_selecionado = []
    for indice, disciplina in enumerate(disciplinas_periodo_selecionado):
        notas_periodo_selecionado.append({'disciplina': disciplina})

        for nota in notas:
            if nota.disciplina.id == disciplina.id:
                notas_periodo_selecionado[indice] = nota

    context = {
        'aluno': aluno,
        'disciplinas': disciplinas_periodo_selecionado,
        'periodos': periodos_ate_o_atual,
        'periodo_selecionado': periodo,
        'notas': notas_periodo_selecionado
    }

    return render(request, 'alunos/listar_notas.html', context)


def cadastrar_nota(request, id, disciplina_id):
    aluno = Aluno.objects.get(pk=id)
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    form = NotaForm(request.POST or None, aluno_default=aluno,
                    disciplina_default=disciplina)

    if form.is_valid():
        form.save()
        return redirect('listar_notas', id, disciplina.periodo_requerido)

    context = {
        'aluno': aluno,
        'disciplina': disciplina,
        'form': form
    }

    return render(request, 'alunos/cadastrar_nota.html', context)


def editar_nota(request, id):
    nota = Nota.objects.get(pk=id)

    form = NotaForm(request.POST or None, instance=nota)

    if form.is_valid():
        form.save()
        return redirect('listar_notas', nota.aluno.id, nota.disciplina.periodo_requerido)

    context = {
        'aluno': nota.aluno,
        'disciplina': nota.disciplina,
        'form': form
    }

    return render(request, 'alunos/cadastrar_nota.html', context)


def remover_nota(request, id, disciplina_id):
    aluno = Aluno.objects.get(pk=id)
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    nota = Nota.objects.filter(aluno=aluno, disciplina=disciplina).first()
    nota.delete()

    return redirect('listar_notas', id, disciplina.periodo_requerido)
