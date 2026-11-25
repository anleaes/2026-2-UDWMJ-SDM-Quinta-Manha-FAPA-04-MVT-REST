from django.shortcuts import render,redirect
from .forms import ConsultaForm
from .models import Consulta

# Create your views here.

def add_consulta(request):
    template_name = 'consultas/adicionar_consulta.html'
    context = {}
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('consultas:list_consulta')
    form = ConsultaForm()
    context ['form'] = form
    return render(request,template_name,context)

def list_consulta(request):
    template_name = 'consultas/lista_consulta.html'
    consultas = Consulta.objects.filter()
    context = {
        'consultas' : consultas
    }
    return render(request, template_name, context)

def menu_consulta(request):
    template_name = 'consultas/menu_consulta.html'
    context = {}
    return render(request, template_name, context)