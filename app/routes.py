from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import app, db
from app.forms import UsuarioForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    form = UsuarioForm(request.form)
    if request.method == "POST" and form.validate: # FAZER O LOGIN (CONTROLADOR)
        return render_template("perfil/perfil.html")
    else: # MOSTRAR O FORMULÁRIO DE LOGIN
        return render_template("login/login.html", form = form)

@app.route('/cadastro', methods=["POST", "GET"])
def cadastro():
    form = UsuarioForm(request.form)
    if request.method == "POST" and form.validate: # FAZER O LOGIN (CONTROLADOR)
        return render_template("perfil/perfil.html")
    else: # MOSTRAR O FORMULÁRIO DE LOGIN
        return render_template("login/cadastro.html", form = form)

@app.route('/perfil')
@login_required
def perfil():
    return f'perfil uuuu DO {current_user.username}' # A FAZER

@app.route('/post')
def post():
    return render_template('post/post.html')