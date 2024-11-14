from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostsForm
from .models import DinoTipoDeDino, DinoEpoca, DinoDieta, DinoBioma
from django.http import JsonResponse
from .forms import DinoForm  # Supondo que você tenha um formulário Django

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
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        print("Dados recebidos:", request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'O post foi criado com sucesso')
            return HttpResponseRedirect(reverse('index'))  # Redireciona para a lista de dinossauros
        else:
            print("Erros no formulário:", form.errors)
    else:
        form = PostsForm()

    # Buscando biomas do banco de dados
    biomas = DinoBioma.objects.all()
    return render(request, 'post-form.html', {"form": form, "biomas": biomas})

def post_detail(request, id):
    template_name = 'post-detail.html'  # Define o nome do template que será usado para renderizar a página de detalhes.
    post = Post.objects.get(id=id)  # Usa o método get para buscar o post com o ID fornecido. Se não for encontrado, levantará uma exceção.
    context = {  # Cria um dicionário de contexto para passar dados para o template.
        'post': post  # Inclui o objeto post no contexto, que será usado no template.
    }
    return render(request, template_name, context)  # Renderiza o template com o contexto fornecido e retorna a resposta HTTP.

def get_options(request):
    tipos = list(DinoTipoDeDino.objects.values('id', 'nome'))
    epocas = list(DinoEpoca.objects.values('id', 'nome'))
    dietas = list(DinoDieta.objects.values('id', 'nome'))

    return JsonResponse({
        'tipos': tipos,
        'epocas': epocas,
        'dietas': dietas,
    })

def create_dino(request):
    if request.method == 'POST':
        form = DinoForm(request.POST, request.FILES)
        print("Dados recebidos para criar dino:", request.POST)  # Print dos dados recebidos
        if form.is_valid():
            form.save()  # Salva o dinossauro no banco de dados
            messages.success(request, 'Dinossauro criado com sucesso!')  # Mensagem de sucesso
            return redirect('index')  # Redireciona para a lista de dinossauros
        else:
            print("Erros no formulário de criação de dino:", form.errors)  # Print dos erros do formulário
    else:
        form = DinoForm()
    
    return render(request, 'post_app/post-form.html', {'form': form})