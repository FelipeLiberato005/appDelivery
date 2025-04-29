from flask import Flask, render_template, request, redirect, url_for
#from auth import verificar_usuario, gerar_log_autenticacao
#from logs import gravar_log
import datetime

app = Flask(__name__)

# Configuração de uma lista simples para simular banco de dados de usuários
usuarios = {
    "user1": "senha123",
    "user2": "senha456",
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        ip_usuario = request.remote_addr
        
        # Verificação do usuário
        if verificar_usuario(usuario, senha, usuarios):
            gerar_log_autenticacao(usuario, ip_usuario, sucesso=True)
            return redirect(url_for("sucesso"))
        else:
            gerar_log_autenticacao(usuario, ip_usuario, sucesso=False)
            return render_template("login.html", mensagem="Credenciais inválidas.")
    
    return render_template("login.html")

@app.route("/sucesso")
def sucesso():
    return "Login realizado com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
