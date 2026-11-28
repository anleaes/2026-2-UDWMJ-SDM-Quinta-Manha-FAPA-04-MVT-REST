from django.shortcuts import render,redirect, get_object_or_404
from .forms import Plano_saudeForm
from .models import Plano_saude

# Create your views here.

def add_plano_saude(request):
    template_name = 'planos_saude/adicionar_plano_saude.html'
    context = {}
    if request.method == 'POST':
        form = Plano_saudeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('planos_saude:list_plano_saude')
    form = Plano_saudeForm()
    context ['form'] = form
    return render(request, template_name, context)

def list_plano_saude(request):
    template_name = 'planos_saude/lista_plano_saude.html'
    planos_saude = Plano_saude.objects.filter()
    context = {
        'planos_saude' : planos_saude
    }
    return render(request, template_name, context)

def menu_plano_saude(request):
    template_name = 'planos_saude/menu_plano_saude.html'
    context = {}
    return render(request, template_name, context)

def delete_plano_saude(request, id_planosaude):
    plano_saude = Plano_saude.objects.get(id=id_planosaude)
    plano_saude.delete()
    return redirect('planos_saude:list_plano_saude')

def edit_plano_saude(request, id_planosaude):
    template_name = 'planos_saude/adicionar_plano_saude.html'
    context ={}
    plano_saude = get_object_or_404(Plano_saude, id=id_planosaude)
    if request.method == 'POST':
        form = Plano_saudeForm(request.POST, instance=plano_saude)
        if form.is_valid():
            form.save()
            return redirect('planos_saude:list_plano_saude')
    form = Plano_saudeForm(instance=plano_saude)
    context ['form'] = form
    return render(request, template_name, context)

