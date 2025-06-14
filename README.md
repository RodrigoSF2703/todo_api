# 📌 To-Do API

API RESTful simples para gerenciamento de tarefas (To-Do List), desenvolvida com **FastAPI** e **PostgreSQL**.

---

## 🚀 Funcionalidades

- ✅ **CRUD de tarefas**: Criar, listar, atualizar e excluir tarefas.
- 🔐 **Autenticação via token estático**.
- 🗂️ **Estrutura modularizada** com separação de responsabilidades.
- 🛡️ **Validação de dados** e tratamento de erros.
- 🐘 **Persistência com PostgreSQL**.
- 🐳 Suporte completo a **Docker e Docker Compose**.

---

## 📦 Instalação e Execução Local (usando Docker)

### Pré-requisitos

- Docker
- Docker Compose

### Clone o repositório

```bash
   git clone https://github.com/RodrigoSF2703/todo_api.git
cd todo_api
```

### Suba os containers

```bash
   docker-compose up --build
```

A aplicação estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Autenticação

Todas as rotas (exceto `/auth/verify-token`) requerem um **token estático**:

### Token padrão:

```
Bearer secret-token
```

Envie este token no header `Authorization`:

```http
Authorization: Bearer secret-token
```

---

## 📘 Documentação Interativa

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Exemplos de Uso (cURL)

### ✅ Criar uma tarefa

```bash
   curl -X POST http://localhost:8000/tasks/ \
-H "Authorization: Bearer secret-token" \
-H "Content-Type: application/json" \
-d '{"title": "Comprar leite", "description": "No mercado", "completed": false}'
```

### 📋 Listar tarefas

```bash
   curl -H "Authorization: Bearer secret-token" http://localhost:8000/tasks/
```

### 🔎 Obter tarefa por ID

```bash
   curl -H "Authorization: Bearer secret-token" http://localhost:8000/tasks/1
```

### ✏️ Atualizar tarefa

```bash
   curl -X PUT http://localhost:8000/tasks/1 \
-H "Authorization: Bearer secret-token" \
-H "Content-Type: application/json" \
-d '{"completed": true}'
```

### ❌ Deletar tarefa

```bash
   curl -X DELETE -H "Authorization: Bearer secret-token" http://localhost:8000/tasks/1
```

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` com:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
```

---

## 🐘 Banco de Dados (PostgreSQL)

A estrutura do banco de dados é criada automaticamente na inicialização da API.

---

## 🛠️ Estrutura do Projeto

```
todo_api/
├── app/
│   ├── api/         # Rotas
│   ├── models/      # Models SQLAlchemy
│   ├── schemas/     # Schemas Pydantic
│   ├── services/    # Lógica de negócio
│   ├── main.py      # App principal
│   └── database.py  # Configuração do banco
├── scripts/
│   └── wait_for_db.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ✅ Testes Rápidos

Use a interface Swagger para testar diretamente via navegador após o deploy:

📍 `http://localhost:8000/docs`

---

## ☁️ Deploy no Render  
A aplicação pode ser facilmente hospedada no Render, uma plataforma moderna de deploy para aplicações web com suporte a serviços backend e banco de dados.

### 🔗 Acesse o app em produção  
👉 https://todo-api-rendersite.onrender.com  
(Substitua pelo seu link real após o deploy)

### 🧰 Configuração no Render  
Para rodar essa API no Render:

- Crie um novo Web Service em https://dashboard.render.com
- Conecte seu repositório GitHub com o projeto
- Defina a variável de ambiente DATABASE_URL com a URL do seu banco PostgreSQL do Render
- Escolha o ambiente: Python 3
- Plano: Free (para testes e uso básico)

### 🐘 Banco de Dados no Render  
Você pode criar um PostgreSQL Managed Database no Render e copiar a URL de conexão gerada para a variável DATABASE_URL.

Exemplo:

```
postgresql://user:password@your-db-host:5432/todo_db
```


## 🧑‍💻 Autor

Rodrigo Souza  
[GitHub](https://github.com/RodrigoSF2703)
