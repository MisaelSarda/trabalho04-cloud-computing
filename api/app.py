from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Caminho para o ficheiro JSON simulando a base de dados
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'doacoes.json')

def carregar_dados():
    """Lê os dados do ficheiro JSON."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/status', methods=['GET'])
def status():
    """Retorna a saúde da aplicação."""
    return jsonify({
        "nome": "API - Sistema de Doacoes",
        "versao": "1.0.0",
        "status": "online"
    }), 200

@app.route('/doacoes', methods=['GET'])
def listar_doacoes():
    """Retorna todos os registos de doações."""
    doacoes = carregar_dados()
    return jsonify(doacoes), 200

@app.route('/doacoes/<int:doacao_id>', methods=['GET'])
def obter_doacao(doacao_id):
    """Retorna uma doação específica pelo seu ID."""
    doacoes = carregar_dados()
    doacao = next((d for d in doacoes if d['id'] == doacao_id), None)
    
    if doacao:
        return jsonify(doacao), 200
    else:
        return jsonify({"erro": "Doacao nao encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)