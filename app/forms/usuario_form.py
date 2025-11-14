from wtforms import Form, StringField, IntegerField, PasswordField, EmailField
from wtforms.validators import DataRequired, length, Email

class UsuarioForm:
    username = StringField("Nome Completo", [DataRequired("Nome obrigatório"), length(min=4, max=255, message="Nome curto ou longo demais")])
    email = EmailField("Email", [DataRequired("Email obrigatório"), Email("Email inválido")])
    password = PasswordField("Senha", [DataRequired()])
    #CONCLUIR FORMULÁRIO