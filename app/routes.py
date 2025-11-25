from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import app, db
from app.forms import UsuarioForm, LoginForm
from app.controllers import UsuarioController, LoginController

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil/perfil.html')

@app.route('/post')
def post():
    return render_template('post/post.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    formulario = LoginForm()
    
    if formulario.validate_on_submit(): # FAZER O LOGIN (CONTROLADOR)
        sucesso = LoginController.login(formulario)
        if sucesso:
            print('SUCESSO NO LOGIN')
            flash('Login feito com sucesso!', category='success')
            return redirect(url_for("index"))
        else:
            print('ERRO NO LOGIN!')
            flash('Erro no login! Email ou senha errados!', category='error')
            return render_template("usuario/login.html", form = formulario)
    
    return render_template("usuario/login.html", form = formulario)
    
@app.route("/logout")
@login_required
def logout():
    LoginController.logout()
    return redirect(url_for('index'))

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
    
    return render_template("usuario/cadastro.html", form = formulario)