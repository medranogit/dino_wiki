from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostsForm
from .models import DinoTipoDeDino, DinoEpoca, DinoDieta, DinoBioma
from django.http import JsonResponse
from .forms import DinoForm  # Supondo que você tenha um formulário Django
from django.core.paginator import Paginator

# As Views no Django são uma parte fundamental do framework e são responsáveis por processar as solicitações HTTP e retornar uma resposta ao cliente. 
# Em termos simples, uma view recebe uma solicitação (request), interage com o modelo (se necessário), e retorna uma resposta, que geralmente é uma página HTML, um arquivo JSON, ou até mesmo uma mensagem de erro.

# Create your views here.

def post_list(request):
    template_name = 'index.html'
    post_list = Post.objects.all()
    
    # Criar um objeto Paginator com 8 itens por página
    paginator = Paginator(post_list, 8)
    
    # Pegar o número da página da query string
    page = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page)
    except:
        posts = paginator.page(1)
    
    context = {
        'posts': posts,
        'page_range': paginator.page_range
    }
    return render(request, template_name, context)

def dino_add(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dinossauro criado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PostsForm()
    
    return render(request, 'dino_add.html', {
        'form': form,
        'tipos': DinoTipoDeDino.objects.all(),
        'epocas': DinoEpoca.objects.all(),
        'dietas': DinoDieta.objects.all(),
        'biomas': DinoBioma.objects.all(),
    })

def dino_detail(request, id):
    template_name = 'dino_detail.html'  # Match the actual file name
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, template_name, context)

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
    
    return render(request, 'post_app/dino_add.html', {'form': form})