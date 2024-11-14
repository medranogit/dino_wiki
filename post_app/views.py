from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostsForm

# As Views no Django são uma parte fundamental do framework e são responsáveis por processar as solicitações HTTP e retornar uma resposta ao cliente. 
# Em termos simples, uma view recebe uma solicitação (request), interage com o modelo (se necessário), e retorna uma resposta, que geralmente é uma página HTML, um arquivo JSON, ou até mesmo uma mensagem de erro.

# Create your views here.

def post_list(request):
    template_name = 'index.html'  # Altere para 'index.html'
    posts = Post.objects.all()  # Obtém todas as instâncias do modelo 'Posts'.
    context = {
        'posts': posts  # Passa a lista de postagens como uma variável 'posts' para o template.
    }
    return render(request, template_name, context)  # Renderiza o template 'index.html' com o contexto fornecido.

def post_create(request):
    if request.method == 'POST': # para metodo POST
        form = PostsForm(request.POST, request.FILES) # pega as informações do form
        if form.is_valid(): # se for valido
            form = form.save(commit=False)
            form.save() # salva
            
            messages.success(request, 'O post foi criado com sucesso') # mensagem quando cria o post
            return HttpResponseRedirect(reverse('post-list')) # coloquei para retornar post-list
        
    form = PostsForm() # senão carrega o formulario  
    return render(request, 'post-form.html', {"form": form}) # nesse template

def post_detail(request, id):
    template_name = 'post-detail.html'  # Define o nome do template que será usado para renderizar a página de detalhes.
    post = Post.objects.get(id=id)  # Usa o método get para buscar o post com o ID fornecido. Se não for encontrado, levantará uma exceção.
    context = {  # Cria um dicionário de contexto para passar dados para o template.
        'post': post  # Inclui o objeto post no contexto, que será usado no template.
    }
    return render(request, template_name, context)  # Renderiza o template com o contexto fornecido e retorna a resposta HTTP.
