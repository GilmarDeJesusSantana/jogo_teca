from flask import Flask, render_template, request, redirect, session, flash, url_for

from jogos import Jogos
from usuarios import Usuarios
from dao import JogoDao
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '0.0.0.0'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'teluni12'
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

jogo_dao = JogoDao(db)

jogo1 = Jogos('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogos('Good of War', 'Rack n Slash', 'PS2')
jogo3 = Jogos('Mortal Kombat', 'Luta', 'Snes')
lista_jogos = [jogo1, jogo2, jogo3]

usuario1 = Usuarios('Gilmar', 'Gil', 'Nao_sei')
usuario2 = Usuarios('Renata', 'Negona', 'Sei_la')
usuario3 = Usuarios('Gilmara', 'Magrela', 'Esta_perdida')

usuarios = {
    usuario1.nickname : usuario1,
    usuario2.nickname : usuario2,
    usuario3.nickname : usuario3
}

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/cadastro-de-jogos')
def cadastro_de_jogos():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastro_de_jogos')))
    nome_formulario = 'Cadastro de Jogos'
    return render_template('cadastro_de_jogos.html', titulo=nome_formulario)


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['Post'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso.')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado!')
    return redirect(url_for('login'))


app.secret_key = 'Gilmar'
app.run(debug=True)
