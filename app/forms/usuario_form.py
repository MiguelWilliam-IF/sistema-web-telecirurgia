from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length, Email

class UsuarioForm(FlaskForm):
    username = StringField("Nome Completo", [DataRequired("Nome obrigatório"), length(min=4, max=255, message="Nome curto ou longo demais")])
    email = EmailField("Email", [DataRequired("Email obrigatório"), Email("Email inválido")])
    password = PasswordField("Senha", [DataRequired()])
    type_user = RadioField("Tipo de Usuário", validators=[DataRequired()], choices=[('externo', 'Externo'), ('aluno', 'Aluno'), ('servidor', 'Servidor')])
    remember_me = BooleanField("Lembrar de mim")
    submit = SubmitField("Salvar")