from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import app, db
from app.forms import UsuarioForm
from app.controllers import UsuarioController

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    formulario = UsuarioForm()
    if formulario.validate_on_submit(): # FAZER O LOGIN (CONTROLADOR)
        return render_template("perfil/perfil.html")
    else: # MOSTRAR O FORMULÁRIO DE LOGIN
        return render_template("usuario/login.html", form = formulario)

@app.route('/cadastro', methods=["POST", "GET"])
def cadastro():
    formulario = UsuarioForm()
    
    if formulario.validate_on_submit(): # FAZER O CADASTRO (CONTROLADOR)
        print('VALIDANDO...')
        sucesso = UsuarioController.salvar(formulario)
        if sucesso:
            print('SUCESSO NO CADASTRO DO USUÁRIO!')
            flash('Cadastro realizado com sucesso!', category='success')
            return redirect(url_for('index'))
        else:
            print('ERRO NO CADASTRO DO USUÁRIO!')
            flash('Erro na realização do cadastro!', category='error')
            return render_template("usuario/cadastro.html", form = formulario)
    
    print('Eh get')
    return render_template("usuario/cadastro.html", form = formulario)

@app.route('/perfil')
@login_required
def perfil():
    return f'perfil uuuu DO {current_user.username}' # A FAZER

@app.route('/post')
def post():
    return render_template('post/post.html')