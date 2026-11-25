from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('menu/', views.menu_paciente, name = 'menu_paciente'),
    path('adicionar/', views.add_paciente, name = 'add_paciente'),
    path('lista/', views.list_paciente,  name ='list_paciente'),
    
]