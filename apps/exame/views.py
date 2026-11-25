from django.shortcuts import render,redirect
from .forms import ExameForm
from .models import Exame

# Create your views here.

def add_exame(request):
    template_name = 'exames/adicionar_exame.html'
    context = {}
    if request.method == "POST":
        form = ExameForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('exames:list_exame')
    form = ExameForm()
    context ['form'] = form
    return render(request, template_name, context)

def list_exame(request):
    template_name = 'exames/lista_exame.html'
    exames = Exame.objects.filter()
    context = {
        'exames' : exames
    }
    return render(request, template_name, context)

def menu_exame(request):
    template_name = 'exames/menu_exame.html'
    context = {}
    return render(request, template_name, context)

