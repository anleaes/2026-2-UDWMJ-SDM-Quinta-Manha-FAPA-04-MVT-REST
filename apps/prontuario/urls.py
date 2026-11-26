from django.urls import path
from . import views 

app_name = 'prontuarios'

urlpatterns = [
   path('adicionar/',views.add_prontuario, name = 'add_prontuario'),
   path('lista/', views.list_prontuario, name = 'list_prontuario'),
   path('menu/', views.menu_prontuario, name = 'menu_prontuario'),
]