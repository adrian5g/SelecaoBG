from django.db import models

"""
CURSO
nome: texto
limite: inteiro
quantidade_de_periodos: inteiro

ALUNO
nome: texto
curso: id
periodo_atual: inteiro

DISCIPLINA
nome: texto
curso: id
periodo_requerido: inteiro

NOTA
valor: decimal
aluno: id
disciplina: id
"""

# Not Null nos parâmetros
# Unique no nome do Aluno
# Unique no nome do Curso
# [X] Colocar a logo numa pasta img
# mudar o ondelete do curso no Model Disciplina para para cascade
# em Nota, (Disciplina e Aluno) precisam ser únicos
# mudar o max digits pra 5


"""
class Curso(models.Model):
    nome = models.CharField('Nome', max_length=300, unique=True, null=False, blank=False)
    vagas = models.IntegerField('Vagas', null=False, blank=False)
    periodos = models.IntegerField('Períodos', null=False, blank=False)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=300, unique=True, null=False, blank=False)
    periodo_atual = models.IntegerField('Período Atual', null=False, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=300, null=False, blank=False)
    periodo_requerido = models.IntegerField('Período Requerido', null=False, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nome


class Nota(models.Model):
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=5, null=False, blank=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=False, blank=False)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        unique_together = ('aluno', 'disciplina')

    def __str__(self):
        return self.valor
"""


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=300)
    vagas = models.IntegerField('Vagas')
    periodos = models.IntegerField('Perídos')

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=300)
    periodo_atual = models.IntegerField('Perído Atual')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=300)
    periodo_requerido = models.IntegerField('Perído Requerido')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Nota(models.Model):
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=3)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
