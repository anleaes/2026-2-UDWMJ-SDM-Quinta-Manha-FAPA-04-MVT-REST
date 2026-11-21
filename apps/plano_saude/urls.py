from django.urls import path
from . import views

app_name = 'planos_saude'

urlpatterns = [
    path('adicionar/', views.add_plano_saude, name = 'add_plano_saude'),
    path('lista/', views.list_plano_saude, name = 'list_plano_saude'),
    path('menu/', views.menu_plano_saude, name = 'menu_plano_saude'),

]