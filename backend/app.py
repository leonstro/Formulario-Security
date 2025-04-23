from flask import Flask, request, jsonify
from auth import gerar_token, validar_token
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
usuarios = {}

CHAVE_IAM = "123456"

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip()
    senha = dados.get("senha", "")

    
    if len(nome) < 3:
        return jsonify({"message": "Nome deve ter pelo menos 3 caracteres."}), 400

    import re
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        return jsonify({"message": "E-mail inválido."}), 400

    if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", senha):
        return jsonify({"message": "Senha fraca."}), 400

    if email in usuarios:
        return jsonify({"message": "Usuário já cadastrado."}), 400

    token = gerar_token(email)
    usuarios[email] = {"nome": nome, "senha": senha, "token": token}
    return jsonify({"message": "Cadastro realizado com sucesso!", "token": token}), 200

@app.route("/acesso-restrito", methods=["GET"])
def acesso():
    
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if validar_token(token):
        return jsonify({"message": "Acesso autorizado via JWT."}), 200

    
    api_key = request.headers.get("x-api-key", "")
    if api_key == CHAVE_IAM:
        return jsonify({"message": "Acesso autorizado via IAM."}), 200

    return jsonify({"message": "Acesso negado. Token ou chave inválida."}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
