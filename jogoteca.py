from flask import render_template, request, redirect, session, flash, url_for

from jogos import Jogos
from dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL
from setup_app import setup_app

app = setup_app()
db = MySQL(app)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista_jogos = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/cadastro-de-jogos')
def cadastro_de_jogos():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastro_de_jogos')))
    nome_formulario = 'Cadastro de Jogos'
    return render_template('cadastro_de_jogos.html', titulo=nome_formulario)


@app.route('/editar-jogos/<int:id>')
def editar_jogos(id):
    nome_formulario = 'Edição de Jogo.'

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar_jogos')))
    jogo = jogo_dao.busca_por_id(id)
    return render_template('editar_jogos.html', titulo=nome_formulario, jogo=jogo)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    id = request.form['id']
    jogo = Jogos(nome, categoria, console, id)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar_jogos(id):
    flash('Jogo deletado!')
    jogo_dao.deletar(id)
    return redirect(url_for('index'))

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    jogo_dao.salvar(jogo)
    arquivo = request.files['arquivo']
    arquivo.save(f'uploads/{arquivo.filename}')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['Post'])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
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
