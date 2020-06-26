from core.models import Professor
from django import forms

class ProfessorForm(forms.ModelForm):
    class Meta:

        model = Professor
        fields = ['Nome', 'Exeperiencia_profissional', 'Hora_aula', 'Disponibilidade']