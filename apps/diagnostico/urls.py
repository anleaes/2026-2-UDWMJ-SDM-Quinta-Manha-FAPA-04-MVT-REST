from django.urls import path
from . import views

app_name = 'diagnosticos'

urlpatterns = [
    path('menu/', views.menu_diagnostico, name = 'menu_diagnostico'),
    path('adicionar/', views.add_diagnostico, name = 'add_diagnostico'),
    path('lista/', views.list_diagnostico, name = 'list_diagnostico'),
    path('editar/<int:id_diagnostico>/', views.edit_diagnostico, name = 'edit_diagnostico'),
    path('excluir/<int:id_diagnostico>/', views.delete_diagnostico, name = 'delete_diagnostico'),
]