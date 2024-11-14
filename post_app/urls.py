from django.urls import path  # Importa a função 'path' do Django, usada para definir padrões de URL.
from . import views  # Importa o módulo 'views' do aplicativo atual, onde estão definidas as views.

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post-create/', views.post_create, name='post-create'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
]