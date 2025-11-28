from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import app, db
from app.forms import UsuarioForm, LoginForm, PostForm
from app.controllers import UsuarioController, LoginController, PostController

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil/perfil.html', posts = PostController.getPostsByUserID(current_user.id))

@app.route('/post')
def post():
    return render_template('post/post.html', posts = PostController.listarPosts())

@app.route('/post/delete/<int:id>')
@login_required
def deletePost(id):
    if current_user.id != PostController.getPostByID(id).user_id:
        print('ERRO! USUÁRIO NÃO PODE APAGAR POSTAGEM QUE NÃO É SUA.')
        flash("Não foi possível realizar a ação.", category="error")
        return redirect(url_for("perfil"))
    
    sucesso = PostController.deletePost(id)
    if sucesso:
        flash("Postagem apagada!", category="success")
        return redirect(url_for('perfil'))
    
    flash('Erro em apagar a postagem.', category='error')
    return redirect(url_for('perfil'))
    
@app.route('/post/edit/<int:id>')
@login_required
def editPost(id):
    if current_user.id != PostController.getPostByID(id).user_id:
        print('ERRO! USUÁRIO NÃO PODE EDITAR POSTAGEM QUE NÃO É SUA.')
        flash("Não foi possível realizar a ação.", category="error")
        return redirect(url_for("perfil"))
    #  =======  A FAZER  =========

@app.route('/post/create', methods=["POST", "GET"])
@login_required
def createPost():
    formulario = PostForm()

    if formulario.validate_on_submit():
        sucesso = PostController.novoPost(formulario, current_user)
        if sucesso:
            print('SUCESSO NA CRIAÇÃO DE NOVA POSTAGEM')
            flash('Nova postagem criada!', category='success')
            return redirect(url_for('post'))
        # ELSE:
        print('ERRO NA CRIAÇÃO DE NOVA POSTAGEM')
        flash('Erro na criação de nova postagem!', category='error')
        return render_template('post/create.html', form = formulario)

    return render_template('post/create.html', form = formulario)

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