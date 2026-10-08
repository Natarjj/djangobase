from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página "Contatos"
    path('contato/', views.contato, name='contato'),

      # Rota de cadastro de pessoas
    path('adicionar/', views.adicionar, name='adicionar'),

    # Rota para visualizar uma pessoa pelo ID
    path('pessoa/<int:id>/', views.detalhe, name='detalhe'),

    #Rota para editar uma pessoa única pelo ID
     path('pessoa/<int:id>/editar/', views.editar, name='editar'),

     # Rota para apagar uma pessoa pelo ID
        path('pessoa/<int:id>/deletar/', views.deletar, name='deletar'),
]
  