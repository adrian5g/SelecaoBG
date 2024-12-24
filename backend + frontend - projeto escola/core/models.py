from django.db import models


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=300)
    vagas = models.IntegerField('Vagas')
    periodos = models.IntegerField('Perídos')

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=300)
    periodo_atual = models.IntegerField('Perído Atual')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=300)
    periodo_requerido = models.IntegerField('Perído Requerido')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Nota(models.Model):
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=5)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('aluno', 'disciplina')
