from flask import Flask, request, render_template, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'chave-secreta-qualquer'  # Usado pra flash messages

def validar_dados(nome, email, senha):
    if len(nome) < 3:
        return "O nome precisa ter pelo menos 3 letras."

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Digite um e-mail válido."

    if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", senha):
        return "A senha precisa ter pelo menos 8 caracteres, uma letra maiúscula e um número."

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    erro = validar_dados(nome, email, senha)
    if erro:
        flash(erro)
        return redirect(url_for('index'))

    flash("Cadastro feito com sucesso!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
