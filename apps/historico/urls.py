from django.urls import path
from . import views

app_name = 'historicos'

urlpatterns = [
  path('adicionar/', views.add_historico, name='add_historico'),
  path('lista/', views.list_historico, name ='list_historico'),
  path('editar/<int:id_historico>/', views.edit_historico, name='edit_historico'),
  path('excluir/<int:id_historico>/', views.delete_historico, name ='delete_historico'),
]