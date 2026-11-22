from django.shortcuts import render,redirect
from .forms import AgendamentoForm
from .models import Agendamento

# Create your views here.

def add_agendamento(request):
    template_name = 'agendamentos/adicionar_agendamento.html'
    context = {}
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('agendamentos:list_agendamento')
    form = AgendamentoForm()
    context ['form'] = form
    return render(request,template_name,context)

def list_agendamento(request):
    template_name = 'agendamentos/lista_agendamento.html'
    agendamentos = Agendamento.objects.filter()
    context = {
        'agendamentos' : agendamentos
    }
    return render(request, template_name, context)

def menu_agendamento(request):
    template_name = 'agendamentos/menu_agendamento.html'
    context = {}
    return render(request, template_name, context)