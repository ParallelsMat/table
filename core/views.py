from django.shortcuts import render, redirect, get_object_or_404
from core.forms import  ProfessorForm
from django.contrib import messages
from core.models import  Professor
# Create your views here.

def index(request):
    return render(request, 'index.html')

def professor(request):

    template_name = 'list.html'
    context = {}

    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Professor cadastrado')
            return redirect('list_prof')
    else:
        form = ProfessorForm()

    context = {
        'form':form,
    }

    return render(request, template_name, context)

def list_professor(request):
    profs = Professor.objects.all()
    print(profs)
    context = {

        'profs':profs,
    }
    print(context)
    template_name = 'list_prof.html'

    return render(request, template_name, context)

def update_prof(request,pk):
    prof = get_object_or_404(Professor, pk = pk )

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=prof)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro Atualizado')
            return redirect('list_prof')
    else:
        form = ProfessorForm(instance=prof)
    template_name = 'list.html'
    context = {
        'form':form,
    }

    return render(request, template_name, context)

def del_prof(request,pk):
    prof = get_object_or_404(Professor, pk = pk)
    prof.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('list_prof')

