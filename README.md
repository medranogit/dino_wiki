# DinoList
![image](https://github.com/user-attachments/assets/1169976b-3fe6-407e-b1f3-e9efc306dd6f)

> ⚠️ **Atenção:** Este projeto ainda **não foi finalizado**. Algumas funcionalidades podem estar incompletas ou em desenvolvimento.


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

## Instalação

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/[SEU_USUARIO]/dino_wiki.git
   cd dino_wiki
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

5. **Alimente o banco de dados**:
   ```bash
   python manage.py populate_db
   ```
6. **Crie o SuperAdmin para acessar o painel**:
   ```bash
   python manage.py createsuperuser
   Username: admin
   Email address: seu_email@example.com
   Password: sua_senha
   Password (again): sua_senha_novamente
   Superuser created successfully.
   ```
7. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação em seu navegador**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

