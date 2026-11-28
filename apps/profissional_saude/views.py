from django.shortcuts import render,redirect, get_object_or_404
from .forms import Profissional_saudeForms
from .models import Profissional_saude

# Create your views here.

def add_profissional_saude(request):
    template_name = 'profissionais_saude/adicionar_profissional_saude.html'
    context = {}
    if request.method == 'POST':
        form = Profissional_saudeForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('profissionais_saude:list_profissional_saude')
    form = Profissional_saudeForms()
    context ['form'] = form
    return render(request,template_name,context)

def list_profissional_saude(request):
    template_name = 'profissionais_saude/lista_profissional_saude.html'
    profissionais_saude = Profissional_saude.objects.filter()
    context = {
        'profissionais_saude' : profissionais_saude
    }
    return render(request, template_name, context)

def menu_profissional_saude(request):
    template_name = 'profissionais_saude/menu_profissional_saude.html'
    context = {}
    return render(request, template_name, context)

def delete_profissional_saude(request, id_profissional_saude):
    profissional_saude = Profissional_saude.objects.get(id=id_profissional_saude)
    profissional_saude.delete()
    return redirect('profissionais_saude:list_profissional_saude')

def edit_profissional_saude(request, id_profissional_saude):
    template_name = 'profissionais_saude/adicionar_profissional_saude.html'
    context = {}
    profissional_saude = get_object_or_404(Profissional_saude, id=id_profissional_saude)
    if request.method == 'POST':
        form = Profissional_saudeForms(request.POST, instance = profissional_saude)
        if form.is_valid():
            form.save()
            return redirect('profissionais_saude:list_profissional_saude')
    form = Profissional_saudeForms(instance=profissional_saude)
    context ['form'] = form
    return render(request, template_name, context)