from flask import Flask, render_template, url_for, request, redirect
import csv
import os

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form['nome']
    matricula = request.form['matricula']
    mensagem = request.form['mensagem']

    data = [nome, matricula, mensagem]
    headers = ['Nome', 'Matricula', 'Mensagem']

    if mensagem != "abacate":
        return redirect('/mensagem-invalida')

    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/alunos.csv', 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        if os.stat('data/alunos.csv').st_size == 0:
            writer.writerow(headers)
        writer.writerow(data)

    return redirect('/confirmacao')

if __name__ == "__main__":
    app.run(debug=True)

# configuração para arquivos estáticos
app.static_folder = 'static'
app.add_url_rule('/static/<path:filename>', endpoint='static', view_func=app.send_static_file)