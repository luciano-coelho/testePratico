# Teste Prático Backend

Projeto de API RESTful para gerenciamento de tarefas.

## Tecnologias Utilizadas

- Django e Django REST Framework
- Django Simple JWT
- SQLite
- Docker
- pytest

## Funcionalidades

1. **CRUD de Tarefas**: Criar, listar, atualizar e excluir tarefas.
2. **Categorias de Tarefas**: Organização das tarefas por categoria.
3. **Autenticação JWT**: Autenticação para acesso seguro aos endpoints.
4. **Compartilhamento de Tarefas**: Permite compartilhar tarefas com outros usuários.
5. **Paginação e Filtros**: Retorna listas paginadas de tarefas.

## Pré-requisitos

- **Python 3.12**
- **Virtualenv**
- **Docker**

## Configuração do Projeto

1. **Clone o repositório**:

   ```bash
    git clone https://github.com/luciano-coelho/testePraticoFront.git
    cd testePraticoFront

2. **Crie e ative um ambiente virtual**:
    ```bash
    python -m venv venv

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt

4. **Crie um arquivo .env com as configurações**:
    ```bash
    DJANGO_SECRET_KEY='chave-secreta'
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:3001

5. **Configuração do Banco de Dados**:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser

6. **Rode o servidor**:
    ```bash
    python manage.py runserver

7. **Iniciar container** 
    ```bash
    docker-compose up --build

8. **Executar testes** 
    ```bash
    pytest

## Documentação dos Endpoints

**Autenticação:**
- **Obter Token:**: POST /api/token/
- **Atualizar Token:**: POST /api/token/refresh/

**Usuários:**
- **Registrar Usuário:**: POST /api/register/

**Tarefas:**
- **Listar Tarefas:** GET /api/tasks/
- **Criar Tarefa:** POST /api/tasks/
- **Detalhar Tarefa:** GET /api/tasks/<id>/
- **Atualizar Tarefa:** PUT /api/tasks/<id>/
- **Excluir Tarefa:** DELETE /api/tasks/<id>/
- **Marcar como Completa/Incompleta:** PATCH /api/tasks/<id>/toggle_complete/
- **Compartilhar Tarefa com Usuário:** POST /api/tasks/<id>/share/

**Categorias:**
- **Listar Categorias:** GET /api/categories/
- **Criar Categoria:** POST /api/categories/
- **Atualizar Categoria:** PATCH /api/categories/<id>/
- **Excluir Categoria:** DELETE /api/categories/<id>/

## Decisões de design
- **Django REST Framework:** Facilidade no desenvolvimento de APIs e integração com Django.
- **JWT para Autenticação:** Permite um fluxo seguro para autenticação sem manter estado no servidor.
- **Paginação e Filtros:** Implementado para melhorar a performance em respostas de listas grandes.
- **Docker:** Facilita a configuração e implantação do ambiente de desenvolvimento.
