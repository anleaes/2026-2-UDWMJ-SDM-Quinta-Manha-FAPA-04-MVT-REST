from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecepcionistaForm
from .models import Recepcionista

# Create your views here.

def add_recepcionista(request):
    template_name = 'recepcionistas/adicionar_recepcionista.html'
    context = {}
    if request.method == "POST":
        form = RecepcionistaForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('recepcionistas:list_recepcionista')
    form = RecepcionistaForm()
    context ['form'] = form
    return render(request, template_name, context)

def list_recepcionista(request):
    template_name = 'recepcionistas/lista_recepcionista.html'
    recepcionistas = Recepcionista.objects.filter()
    context = {
        'recepcionistas' : recepcionistas
    }
    return render(request,template_name,context)

def menu_recepcionista(request):
    template_name = 'recepcionistas/menu_recepcionista.html'
    context = {}
    return render(request, template_name, context)

def delete_recepcionista(request, id_recepcionista):
    recepcionista = Recepcionista.objects.get(id=id_recepcionista)
    recepcionista.delete()
    return redirect('recepcionistas:list_recepcionista')

def edit_recepcionista(request, id_recepcionista):
    template_name = 'recepcionistas/adicionar_recepcionista.html'
    context ={}
    recepcionista = get_object_or_404(Recepcionista, id=id_recepcionista)
    if request.method == 'POST':
        form = RecepcionistaForm(request.POST, instance=recepcionista)
        if form.is_valid():
            form.save()
            return redirect('recepcionistas:list_recepcionista')
    form = RecepcionistaForm(instance=recepcionista)
    context ['form'] = form
    return render(request, template_name, context)
