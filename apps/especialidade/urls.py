from django.urls import path
from . import views

app_name = 'especialidades'

urlpatterns = [
    path('adicionar/',views.add_especialidade, name='add_especialidade'),
    path('lista/',views.list_especialidade, name='list_especialidade'),
    path('menu/',views.menu_especialidade, name='menu_especialidade'),
    path('deletar/<int:id_especialidade>/', views.delete_especialidade, name='delete_especialidade'),
]