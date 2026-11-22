from django.urls import path
from . import views

app_name = 'agendamentos'

urlpatterns = [
    path('menu/', views.menu_agendamento, name = 'menu_agendamento'),
    path('adicionar/', views.add_agendamento, name = 'add_agendamento'),
    path('lista/', views.list_agendamento,  name ='list_agendamento'),
    
]