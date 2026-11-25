from django.urls import path
from . import views

app_name = 'recepcionistas'

urlpatterns = [
    path('adicionar/', views.add_recepcionista, name='add_recepcionista'),
    path('lista/', views.list_recepcionista, name='list_recepcionista'),
    path('menu/', views.menu_recepcionista, name='menu_recepcionista'),
]