from django.db import models

# Create your models here.

class Professor(models.Model):
    STATUS_CHOICES = (
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno'),
    )
    Nome = models.CharField(max_length=100, verbose_name='Nome do professor')
    Exeperiencia_profissional = models.CharField('experiencia', max_length=200)
    Hora_aula = models.TimeField('Tempo', blank=True)
    Disponibilidade = models.IntegerField('Selecione o turno', choices=STATUS_CHOICES, default=1, blank=True)


    def __str__(self):
        return self.Nome

    class Meta:
        db_table = 'professor'
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
        ordering = ['Nome']

class Disciplina(models.Model):
    Nome_Disciplina = models.TextField(max_length=25, verbose_name='Disciplina')
    carga_horaria = models.IntegerField(verbose_name='Carga horaria')

    def __str__(self):
        return self.Nome_Disciplina

    class Meta:
        db_table = 'disciplina'
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'
        ordering = ['Nome_Disciplina']


class Professor_Disciplina(models.Model):
    codigo_prof = models.ForeignKey(Professor, verbose_name='Professor', related_name='professor_disciplina', on_delete=models.CASCADE)
    codigo_disciplina = models.ForeignKey(Disciplina, verbose_name='Disciplina', related_name= 'disciplina_professor', on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=20, verbose_name='Nome do curso')
    semestre = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Semestre')

    def __str__(self):
        return self.nome_curso

    class Meta:
        db_table = 'professor_disciplina'
        verbose_name = 'professor e disciplina'
        verbose_name_plural = 'professores e disciplinas'
