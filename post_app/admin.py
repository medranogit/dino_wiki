from django.contrib import admin
from .models import DinoBioma, DinoEpoca, DinoTipoDeDino, Post, DinoDieta # Importa todos os modelos.


#O arquivo admin.py em um projeto Django é onde você configura a interface de administração para os seus modelos. 
# O Django vem com uma interface de administração pronta, que permite a você gerenciar os dados dos seus modelos diretamente do navegador. 
# Essa interface é muito útil para realizar operações de CRUD (Criar, Ler, Atualizar e Deletar) sem precisar escrever código SQL ou usar o shell do Django.

# Register your models here.

admin.site.register(Post) # Registra o modelo Posts para que apareça no admin
admin.site.register(DinoBioma) # Registra o modelo Bioma para que apareça no admin
admin.site.register(DinoEpoca) # Registra o modelo Epoca Dino para que apareça no admin
admin.site.register(DinoTipoDeDino) # Registra o modelo Tipo de Dino para que apareça no admin
admin.site.register(DinoDieta) # Registra o modelo Tipo de Dino para que apareça no admin


# Migrations
# Depois de definir seus models, você precisa gerar e aplicar migrações para que o Django crie as tabelas no banco de dados. Você faz isso com os comandos:

# python manage.py makemigrations
# python manage.py migrate