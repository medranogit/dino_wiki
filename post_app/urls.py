from django.urls import path  # Importa a função 'path' do Django, usada para definir padrões de URL.
from . import views  # Importa o módulo 'views' do aplicativo atual, onde estão definidas as views.
from .views import get_options, create_dino

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post-create/', views.dino_add, name='dino_add'),
    path('post/<int:id>/', views.dino_detail, name='dino_detail'),
    path('api/get-options/', get_options, name='get_options'),
    path('create/', create_dino, name='create_dino'),
]