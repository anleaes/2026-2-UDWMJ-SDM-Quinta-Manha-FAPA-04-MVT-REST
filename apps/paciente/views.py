from django.shortcuts import render,redirect
from .forms import PacienteForm
from .models import Paciente

# Create your views here.

def add_paciente(request):
    template_name = 'pacientes/adicionar_paciente.html'
    context = {}
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pacientes:list_paciente')
    form = PacienteForm()
    context ['form'] = form
    return render(request,template_name,context)

def list_paciente(request):
    template_name = 'pacientes/lista_paciente.html'
    pacientes = Paciente.objects.filter()
    context = {
        'pacientes' : pacientes
    }
    return render(request, template_name, context)

def menu_paciente(request):
    template_name = 'pacientes/menu_paciente.html'
    context = {}
    return render(request, template_name, context)

def delete_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()
    return redirect('pacientes:list_paciente')
