from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiagnosticoForm
from .models import Diagnostico

# Create your views here.

def add_diagnostico(request):
    template_name = 'diagnosticos/adicionar_diagnostico.html'
    context = {}
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = DiagnosticoForm()
    context ['form'] = form
    return render(request, template_name, context)

def list_diagnostico(request):
    template_name = 'diagnosticos/lista_diagnostico.html'
    diagnosticos = Diagnostico.objects.filter()
    context = {
        'diagnosticos' : diagnosticos
    }
    return render(request, template_name, context)

def edit_diagnostico(request, id_diagnostico):
    template_name = 'diagnosticos/adicionar_diagnostico.html'
    context = {}
    diagnostico = get_object_or_404(Diagnostico, id=id_diagnostico)
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid:
            form.save()
            return redirect('diagnosticos:list_diagnostico')
    form = DiagnosticoForm(instance=diagnostico)
    context['form'] = form
    return render(request, template_name, context)

def delete_diagnostico(request,id_diagnostico):
    diagnostico = Diagnostico.objects.get(id=id_diagnostico)
    diagnostico.delete()
    return redirect('diagnosticos:list_diagnostico')