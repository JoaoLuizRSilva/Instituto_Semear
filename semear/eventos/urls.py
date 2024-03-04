from django.urls import path
from . import views  # Importa as views do aplicativo atual

urlpatterns = [
    path('', views.main),  # URL para a página principal
    path('api/events/', views.get_events, name='get_events'),  # URL para obter todos os eventos
    path('api/events/view/<int:id>', views.get_event, name='get_event'),  # URL para visualizar um evento específico pelo ID
    path('api/events/update/<int:id>', views.update_event, name='update_event'),  # URL para atualizar um evento específico pelo ID
    path('api/events/delete/<int:id>', views.delete_event, name='delete_event'),  # URL para excluir um evento específico pelo ID
    path('create_event/', views.create_event, name='create_event'),  # URL para criar um novo evento
]