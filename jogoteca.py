from flask import Flask, render_template, request, redirect, session, flash

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
    if 'usuario_logado' in session or session['usuario_logado'] == None:
        return redirect('/login')
    nome_formulario = 'Cadastro de Jogos'
    return render_template('cadastro_de_jogos.html', titulo=nome_formulario)


@app.route('/criar', methods=['POST', ])
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
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso.')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado!')
    return redirect('/')


app.secret_key = 'Gilmar'
app.run(debug=True)
