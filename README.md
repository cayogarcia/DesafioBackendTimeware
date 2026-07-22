# 🚀 Desafio Técnico Backend - API REST de Clientes e Pedidos

API REST desenvolvida em Python com **FastAPI** e **SQLAlchemy** para gerenciamento de clientes e pedidos, cobrindo validações de schema, persistência em SQLite, suíte de testes automatizados e pipeline de integração contínua (CI/CD) via GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **ORM & Database:** SQLAlchemy & SQLite
* **Validação de Dados:** Pydantic v2 (com suporte a e-mail)
* **Testes Automatizados:** Pytest & HTTPX
* **CI/CD:** GitHub Actions

---

## 📁 Estrutura do Projeto (Clean Architecture)

A aplicação foi organizada seguindo a separação em camadas para garantir baixo acoplamento e facilidade de manutenção:

.
├── app/
│   ├── api/             # Camada de Entrada / Rotas (Endpoints HTTP)
│   ├── domain/          # Modelos do Banco de Dados (SQLAlchemy)
│   ├── repositories/    # Persistência de Dados (ORM vs SQL Puro)
│   ├── schemas/         # DTOs e Validações de Entrada/Saída (Pydantic)
│   └── services/        # Regras de Negócio e Casos de Uso
├── scripts/             # Scripts DDL e DML em SQL Puro
├── tests/               # Testes Unitários e de Integração (Pytest)
├── .github/workflows/   # Pipeline de CI/CD (GitHub Actions)
├── pytest.ini           # Configurações de execução do Pytest
├── requirements.txt     # Dependências do Projeto
└── main.py              # Ponto de entrada da aplicação

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.11 ou superior instalado.
* Git instalado.

### 1. Clonar o repositório
git clone https://github.com/cayogarcia/DesafioBackendTimeware.git
cd DesafioBackendTimeware

### 2. Criar e ativar o ambiente virtual
* Windows (PowerShell):
  python -m venv venv
  .\venv\Scripts\Activate.ps1

* Linux / macOS:
  python3 -m venv venv
  source venv/bin/activate

### 3. Instalar as dependências
pip install --upgrade pip
pip install -r requirements.txt

### 4. Executar a aplicação
uvicorn app.main:app --reload

A aplicação estará rodando em http://127.0.0.1:8000.

---

## 📑 Documentação Interativa (Swagger)

A documentação da API é gerada automaticamente pelo FastAPI. Com a aplicação rodando, acesse no seu navegador:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

---

## 🧪 Como Executar os Testes Automatizados

Os testes cobrem a criação e listagem de pedidos/clientes utilizando um banco SQLite em memória isolado para os testes.

Para rodar a suíte de testes:
pytest

---

## ⚙️ CI/CD (Continuous Integration)

O repositório conta com um workflow automatizado no **GitHub Actions** (`.github/workflows/ci.yml`). 

A cada `push` ou `pull request` direcionado à branch `main`, a pipeline executa os seguintes passos automaticamente em uma máquina virtual Linux:
1. Setup do ambiente Python 3.11.
2. Instalação de todas as dependências listadas no `requirements.txt`.
3. Execução dos testes automatizados com `pytest`.

---

## 📌 Decisões Técnicas & Boas Práticas

* **Repository Pattern:** Isolamento completo do ORM/consultas do banco em relação às regras de negócio.
* **Consultas Híbridas (ORM vs SQL Puro):** Demonstração do uso de ORM (`SQLAlchemy`) para o CRUD rotineiro e consultas em `SQL Puro` (`text()`) para otimização e performance em relatórios complexos.
* **Conventional Commits:** Histórico de versionamento estruturado com commits semânticos (`feat:`, `fix:`, `ci:`, `test:`).