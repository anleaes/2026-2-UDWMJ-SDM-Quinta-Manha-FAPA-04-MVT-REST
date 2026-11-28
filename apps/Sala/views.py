from django.shortcuts import render,redirect, get_object_or_404
from .forms import SalaForm
from .models import Sala

# Create your views here.

def add_sala(request):
    template_name = 'salas/adicionar_sala.html'
    context = {}
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('salas:list_sala')
    form = SalaForm()
    context ['form'] = form
    return render(request,template_name,context)

def list_sala(request):
    template_name = 'salas/lista_sala.html'
    salas = Sala.objects.filter()
    context = {
        'salas' : salas
    }
    return render(request, template_name, context)

def menu_sala(request):
    template_name = 'salas/menu_sala.html'
    context = {}
    return render(request, template_name, context)

def delete_sala(request, id_sala):
    sala = Sala.objects.get(id=id_sala)
    sala.delete()
    return redirect('salas:list_sala')

def edit_sala(request, id_sala):
    template_name = 'salas/adicionar_sala.html'
    context = {}
    sala = get_object_or_404(Sala, id=id_sala)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance = sala)
        if form.is_valid():
            form.save()
            return redirect('salas:list_sala')
    form = SalaForm(instance=sala)
    context ['form'] = form
    return render(request, template_name, context)