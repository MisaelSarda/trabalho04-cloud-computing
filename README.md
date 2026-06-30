# API - Sistema de Doações (Cloud Computing)

Esta é uma API REST desenvolvida como Trabalho Final da disciplina de Cloud Computing. O sistema simula o gerenciamento de doações de roupas e alimentos.

## Tecnologias Utilizadas
* Python 3
* Flask (Framework Web)
* Pytest (Testes Unitários)
* Docker (Containerização)

## Como executar localmente (SEM container)
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie a API: `python api/app.py`
3. A API estará disponível em `http://127.0.0.1:5000`.

## Como executar localmente (COM container Docker)
1. Construa a imagem: `docker build -t api-doacoes .`
2. Rode o container: `docker run -p 5000:5000 api-doacoes`
3. A API estará disponível em `http://127.0.0.1:5000`.

## Como rodar os testes
Execute o comando: `python -m pytest api/tests/`