from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = EmailField("Email", [DataRequired("Email obrigatório"), Email("Email inválido")])
    password = PasswordField("Senha", [DataRequired()])
    remember_me = BooleanField("Lembrar de mim")