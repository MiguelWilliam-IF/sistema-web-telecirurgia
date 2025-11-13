from flask import Flask, render_template, redirect, url_for, flash, request
from app import app, db

@app.route('/')
def index():
    return 'fucionando yippieee'