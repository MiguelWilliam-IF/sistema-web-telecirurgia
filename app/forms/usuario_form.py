from wtforms import Form, StringField, PasswordField, EmailField, RadioField, BooleanField
from wtforms.validators import DataRequired, length, Email

class UsuarioForm(Form):
    username = StringField("Nome Completo", [DataRequired("Nome obrigatório"), length(min=4, max=255, message="Nome curto ou longo demais")])
    email = EmailField("Email", [DataRequired("Email obrigatório"), Email("Email inválido")])
    password = PasswordField("Senha", [DataRequired()])
    type_user = RadioField("Tipo de Usuário", validators=[DataRequired()], choices=[('externo', 'Externo'), ('aluno', 'Aluno'), ('servidor', 'Servidor')])
    remember = BooleanField("Lembrar de mim", validators=[DataRequired()])