from flask import Flask, render_template, redirect, url_for, flash, request
from app import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login/login.html")

@app.route('/post')
def post():
    return render_template('post/post.html')