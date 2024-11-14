"""
URL configuration for WikiDinos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa o módulo de administração do Django, que fornece a interface administrativa.
from django.conf import settings  # Importa as configurações globais do projeto, como URLs estáticas e de mídia.
from django.conf.urls.static import static  # Importa a função para servir arquivos estáticos e de mídia durante o desenvolvimento.
from django.urls import path, include  # Importa as funções para definir rotas (URLs) e incluir URLs de outros aplicativos.

urlpatterns = [
    path('admin/', admin.site.urls),  # Define a rota para o painel de administração do Django.
    path('', include('post_app.urls')) #Incluindo todas as URLs no app 'post_app'.
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Adiciona a configuração para servir arquivos estáticos (CSS, JS, imagens) durante o desenvolvimento.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adiciona a configuração para servir arquivos de mídia (upload de usuários) durante o desenvolvimento.
