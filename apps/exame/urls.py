from django.urls import path
from . import views

app_name = 'exames'

urlpatterns = [
    path('menu/', views.menu_exame, name = 'menu_exame'),
    path('adicionar/', views.add_exame, name = 'add_exame'),
    path('lista/', views.list_exame,  name ='list_exame'),
    
]