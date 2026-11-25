from django.shortcuts import render, redirect
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
    
