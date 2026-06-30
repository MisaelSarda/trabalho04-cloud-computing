import pytest
from api.app import app

@pytest.fixture
def client():
    """Configura o cliente de testes do Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_rota_status(client):
    """Verifica se a API está online (Status 200)."""
    resposta = client.get('/status')
    assert resposta.status_code == 200
    assert resposta.json['status'] == 'online'

def test_listar_doacoes(client):
    """Verifica se a rota /doacoes devolve uma lista (Status 200)."""
    resposta = client.get('/doacoes')
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)

def test_obter_doacao_sucesso(client):
    """Verifica se encontra a doação ID 1 (Status 200)."""
    resposta = client.get('/doacoes/1')
    assert resposta.status_code == 200
    assert resposta.json['id'] == 1
    assert resposta.json['item'] == 'Arroz 5kg'

def test_obter_doacao_falha(client):
    """Verifica o erro ao buscar um ID que não existe (Status 404)."""
    resposta = client.get('/doacoes/999')
    assert resposta.status_code == 404
    assert 'erro' in resposta.json