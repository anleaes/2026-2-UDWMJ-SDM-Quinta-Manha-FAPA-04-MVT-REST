from django.shortcuts import render,redirect
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