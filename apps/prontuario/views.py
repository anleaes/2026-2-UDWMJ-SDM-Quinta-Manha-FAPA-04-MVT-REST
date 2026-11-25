from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProntuarioForm
from .models import Prontuario

# Create your views here.

def add_prontuario(request):
    template_name = 'prontuarios/adicionar_prontuario.html'
    context ={}
    if request.method == 'POST':
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('prontuarios:list_prontuario')
    form = ProntuarioForm()
    context ['form'] = form
    return render(request, template_name, context)

def list_prontuario(request):
    template_name = 'prontuarios/lista_prontuario.html'
    context = {}
    prontuario = Prontuario.objects.filter()
    context = {
        'prontuarios' : prontuario
    }
    return render(request, template_name, context)

def menu_prontuario(request):
    template_name = 'prontuarios/menu_prontuario.html'
    context = {}
    return render(request,template_name,context)

