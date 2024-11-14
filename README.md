# DinoList

DinoList é uma aplicação web desenvolvida em Django que permite aos usuários visualizar, criar e gerenciar informações sobre dinossauros. A aplicação possui uma interface de administração para gerenciar os dados dos dinossauros, incluindo suas características, dietas e biomas.

## Funcionalidades

- **Listagem de Dinossauros**: Visualize todos os dinossauros cadastrados em uma lista.
- **Detalhes do Dinossauro**: Veja informações detalhadas sobre cada dinossauro, incluindo tipo, dieta, tamanho e peso.
- **Criação de Novos Dinossauros**: Adicione novos dinossauros ao sistema através de um formulário intuitivo.
- **Interface de Administração**: Gerencie os modelos de dinossauros diretamente do painel de administração do Django.
- **Validação de Dados**: Garantia de que os dados inseridos atendem a critérios específicos, como tamanhos e pesos.

## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido de aplicações.
- **HTML/CSS**: Para a estrutura e estilo da interface do usuário.
- **Bootstrap**: Para um design responsivo e moderno.
- **SQLite**: Banco de dados padrão do Django para desenvolvimento.

## Estrutura do Projeto

post_app/
│
├── admin.py               # Configurações da interface de administração
├── apps.py                # Configurações do aplicativo
├── forms.py               # Formulários para criação e edição de dinossauros
├── models.py              # Modelos de dados
├── tests.py               # Testes automatizados
├── urls.py                # Mapeamento de URLs
├── views.py               # Lógica de visualização
├── static/                # Arquivos estáticos (CSS, imagens)
│   ├── css/
│   │   ├── base.css
│   │   ├── post-detail.css
│   │   └── post-list.css
│   └── images/            # Imagens dos dinossauros
└── templates/             # Templates HTML
    ├── base.html
    ├── index.html
    ├── post-detail.html
    ├── post-form.html
    └── _statusMessage.html

## Instalação

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/dinolists.git
   cd dinolists
   ```

2. **Crie um ambiente virtual e ative-o**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações para configurar o banco de dados**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação em seu navegador**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request. Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona uma nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-sua-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com [seu_email@exemplo.com](mailto:seu_email@exemplo.com).

## Screenshots

![Exemplo de Listagem de Dinossauros](static/images/exemplo-listagem.png)
*Exemplo de Listagem de Dinossauros*

![Exemplo de Detalhes do Dinossauro](static/images/exemplo-detalhes.png)
*Exemplo de Detalhes do Dinossauro*