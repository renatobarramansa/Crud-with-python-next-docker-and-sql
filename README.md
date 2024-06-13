# Projeto CRUD com Next.js,Docker, Python e SQL

Este projeto é um aplicativo CRUD (Create, Read, Update, Delete) desenvolvido utilizando Next.js para o frontend, Python com Flask para o backend e SQL como banco de dados. A aplicação serve como um exemplo prático de como integrar essas tecnologias para criar uma aplicação web completa e funcional.

## Funcionalidades

- **Criação de Registros**: Permite a criação de novos registros no banco de dados.
- **Leitura de Registros**: Exibe registros armazenados no banco de dados em uma interface amigável.
- **Atualização de Registros**: Permite a atualização dos dados existentes.
- **Exclusão de Registros**: Permite a remoção de registros do banco de dados.
- **Integração Frontend e Backend**: Demonstra a comunicação entre o frontend em Next.js e o backend em Python através de API RESTful.

## Tecnologias Utilizadas

- **Next.js**: Framework React para a criação do frontend da aplicação, oferecendo renderização do lado do servidor (SSR) e geração de sites estáticos.
- **Python**: Linguagem de programação utilizada no backend para a lógica da aplicação e comunicação com o banco de dados.
- **SQL**: Banco de dados relacional para armazenar e gerenciar os dados da aplicação.
- **SQLAlchemy**: ORM (Object-Relational Mapping) em Python para interagir com o banco de dados SQL de forma mais simples e eficiente.

## Estrutura do Projeto

- **frontend/**: Contém a aplicação Next.js.
- **backend/**: Contém a aplicação Flask com a API e a lógica do servidor.
- **database/**: Contém scripts e arquivos relacionados ao banco de dados.

## Como Executar o Projeto

### Pré-requisitos

- Node.js e npm/yarn
- Python 3 e pip
- Um banco de dados SQL (MySQL, PostgreSQL, SQLite, etc.)

### Passos para Configuração

#### Frontend

1. Navegue até o diretório `frontend`:
   ```bash
   cd frontend



2. Instale as dependências:
   ```bash
   npm install

3. Instale as Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev

#### Backend

1. Instale o as dependências do backEnd:
   ```bash
   cd backend
   pip install -r requirements.txt

2. Navegue até o diretório `backend`:
   ```bash
   cd backend

3. Crie um ambiente virtual
   ```bash
   python -m venv venv

3. Executar o ambiente venv
   ```bash
   source venv/bin/activate


4. Instalar flask
   ```bash
   pip install flask


5. Configurar o arquivo app.py
   ```bash
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello_world():
      return "<p>Servidor flask funcionando</p>"

6. Rodar o servidor flask
   ```bash
   flask --app app.py run


##### Resolução de possiveis problemas
1.    ```bash
      The virtual environment was not created successfully because ensurepip is not
      available.  On Debian/Ubuntu systems, you need to install the python3-venv
      package using the following command.

      sudo apt install python3-venv

      You may need to use sudo with that command.  After installing the python3-venv
      package, recreate your virtual environment.

2. Para listar se as dependências foram instaladas corretamente
      ```bash
      pip list
      
   




   
