from django.forms import ModelForm
from .models import Curso, Disciplina, Aluno, Nota


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'vagas', 'periodos']


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'periodo_requerido', 'curso']

    def __init__(self, *args, **kwargs):
        curso_default = kwargs.pop('curso_default', None)
        super().__init__(*args, **kwargs)
        self.fields['curso'].initial = curso_default


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'periodo_atual', 'curso']


class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = ['valor', 'aluno', 'disciplina']

    def __init__(self, *args, **kwargs):
        aluno_default = kwargs.pop('aluno_default', None)
        disciplina_default = kwargs.pop('disciplina_default', None)
        super().__init__(*args, **kwargs)
        self.fields['aluno'].initial = aluno_default
        self.fields['disciplina'].initial = disciplina_default
