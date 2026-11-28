from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('menu/', views.menu_paciente, name = 'menu_paciente'),
    path('adicionar/', views.add_paciente, name = 'add_paciente'),
    path('lista/', views.list_paciente,  name ='list_paciente'),
    path('editar/<int:id_paciente>/', views.edit_paciente, name ='edit_paciente'),
    path('deletar/<int:id_paciente>/', views.delete_paciente, name='delete_paciente'),
    
]