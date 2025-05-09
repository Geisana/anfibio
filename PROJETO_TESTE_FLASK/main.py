from flask import Flask, render_template

app = Flask(__name__)
#route = caminho depois do domínio
#funcao o que voce quer exibir na pagina
#template
#coloca o site no ar

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)

#servidor do vercel