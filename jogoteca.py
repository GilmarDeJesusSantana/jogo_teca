from flask import Flask, render_template

from jogos import Jogos

app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogos('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogos('Good of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogos('Mortal Kombat', 'Luta', 'Snes')
    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/cadastro-de-jogos')
def cadastro_de_jogos():
    nome_formulario='Cadastro de Jogos'
    return render_template('cadastro_de_jogos.html', titulo=nome_formulario)
app.run()
