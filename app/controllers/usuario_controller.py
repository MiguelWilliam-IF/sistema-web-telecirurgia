from app import db
import sqlalchemy as sa
from app.models import Usuario
from werkzeug.security import generate_password_hash


class UsuarioController:
    def salvar(form):
        try:
            usuario = Usuario()
            form.populate_obj(usuario)
            usuario.password_hash = generate_password_hash(form.password.data)

            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            
            print(f'ERRO NO CADASTRO DE USUÁRIO: {e}')
            return False