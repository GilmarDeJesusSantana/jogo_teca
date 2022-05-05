from flask import Flask, render_template, request, redirect

from jogos import Jogos

app = Flask(__name__)

jogo1 = Jogos('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogos('Good of War', 'Rack n Slash', 'PS2')
jogo3 = Jogos('Mortal Kombat', 'Luta', 'Snes')
lista_jogos = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/cadastro-de-jogos')
def cadastro_de_jogos():
    nome_formulario='Cadastro de Jogos'
    return render_template('cadastro_de_jogos.html', titulo=nome_formulario)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['Post'])
def autenticar():
    if 'alohomora' == request.form['senha']:
        return redirect('/')
    else:
        return redirect('/login')

app.run(debug=True)
