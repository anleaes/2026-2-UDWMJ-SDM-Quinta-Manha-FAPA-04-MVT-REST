from django.shortcuts import render, redirect, get_object_or_404
from .forms import HistoricoForm
from .models import Historico

# Create your views here.

def add_historico(request):
    template_name = 'historicos/adicionar_historico.html'
    context = {}
    if request.method == 'POST':
        form = HistoricoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('historicos:list_historico')
    form = HistoricoForm()
    context ['form'] = form
    return render(request,template_name,context)

def list_historico(request):
    template_name = 'historicos/lista_historico.html'
    historicos = Historico.objects.filter()
    context = {
        'historicos' : historicos
    }
    return render(request, template_name, context)

def edit_historico(request, id_historico):
    template_name = 'historicos/adicionar_historico.html'
    context = {}
    historico = get_object_or_404(Historico, id=id_historico)
    if request.method == 'POST':
        form = HistoricoForm(request.POST, instance=historico)
        if form.is_valid():
            form.save()
            return redirect('historicos:list_historico')
    form = HistoricoForm(instance=historico)
    context['form'] = form
    return render(request, template_name, context)

def delete_historico(request,id_historico):
    historico = Historico.objects.get(id=id_historico)
    historico.delete()
    return redirect('core:home')

def menu_historico(request):
    template_name = 'historicos/menu_historico.html'
    context = {}
    return render(request, template_name, context)



            
            
