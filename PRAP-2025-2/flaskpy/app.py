from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = "p1cl3s.p0c4h0nt4s"

from datetime import datetime, timedelta
SESSION_TIMEOUT = timedelta(minutes=30)

@app.before_request
def check_login():
    allowed_routes = ["login", "index", "static"]
    #Se não tá logado só algumas rotas são permitidas.
    if request.endpoint not in allowed_routes and "nome" not in session:
        return redirect(url_for("index"))
    
    #
    if "nome" in session and "last_seen" in session:
        last_seen = datetime.fromisoformat(session["last_seen"])
        if datetime.now() - last_seen > SESSION_TIMEOUT:
            session.clear()
            return redirect(url_for("index"))
        session["last_seen"] = datetime.now().isoformat()

@app.route("/")
def index():
    if "nome" in session:
        return redirect(url_for("welcome"))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    nome = request.form.get("nome")
    if nome:
        session["nome"] = nome
        session["last_seen"] = datetime.utcnow().isoformat()
        return redirect(url_for("welcome"))
    return redirect(url_for("index"))

@app.route("/welcome")
def welcome():
    nome = session.get("nome")
    return render_template("welcome.html", nome=nome)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
