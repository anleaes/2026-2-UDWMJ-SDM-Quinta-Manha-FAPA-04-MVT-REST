from django.urls import path
from . import views

app_name = 'salas'

urlpatterns = [
    path('menu/', views.menu_sala, name = 'menu_sala'),
    path('adicionar/', views.add_sala, name = 'add_sala'),
    path('lista/', views.list_sala,  name ='list_sala'),
    
]