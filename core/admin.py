from django.contrib import admin
from core.models import Professor, Disciplina, Professor_Disciplina
# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):

    list_display = ['Nome', 'Exeperiencia_profissional', 'Disponibilidade']

admin.site.register(Professor, ProfessorAdmin)


class DisciplinaAdmin(admin.ModelAdmin):


    list_display = ['Nome_Disciplina', 'carga_horaria']


admin.site.register(Disciplina, DisciplinaAdmin)


class Professor_DisciplinaAdmin(admin.ModelAdmin):



    list_display = ['codigo_prof', 'codigo_disciplina', 'nome_curso', 'semestre']


admin.site.register(Professor_Disciplina, Professor_DisciplinaAdmin)