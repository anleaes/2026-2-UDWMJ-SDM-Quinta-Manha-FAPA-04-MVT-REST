from django.urls import path
from . import views

app_name = 'profissionais_saude'

urlpatterns = [
    path('menu/', views.menu_profissional_saude, name = 'menu_profissional_saude'),
    path('adicionar/', views.add_profissional_saude, name = 'add_profissional_saude'),
    path('lista/', views.list_profissional_saude,  name ='list_profissional_saude'),
    path('deletar/<int:id_profissional_saude>/', views.delete_profissional_saude, name='delete_profissional_saude'),
    
]