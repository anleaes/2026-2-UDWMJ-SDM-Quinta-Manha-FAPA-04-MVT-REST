from django.urls import path
from . import views

app_name = 'consultas'

urlpatterns = [
  path('menu/', views.menu_consulta, name= 'menu_consulta'),
  path('adicionar/', views.add_consulta, name='add_consulta'),
  path('lista/', views.list_consulta, name ='list_consulta'),
 
]