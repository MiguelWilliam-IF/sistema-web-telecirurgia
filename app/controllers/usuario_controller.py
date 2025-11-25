from app import db
import sqlalchemy as sa
from app.models import Usuario
from werkzeug.security import generate_password_hash


class UsuarioController:
    def salvar(form):
        try:
            if (UsuarioController.checar_unicidade(form.username.data, 'username') and UsuarioController.checar_unicidade(form.email.data, 'email')):
                usuario = Usuario()
                form.populate_obj(usuario)
                usuario.password_hash = generate_password_hash(form.password.data)

                

                db.session.add(usuario)
                db.session.commit()
                return True
            else:
                print(f'ERRO DE UNICIDADE!! EMAIL OU USERNAME JÁ EXISTEM')
                
                return False
        except Exception as e:
            db.session.rollback()
            
            print(f'ERRO NO CADASTRO DE USUÁRIO: {e}')
            return False
        
    def checar_unicidade(campo, tipo):
        if tipo == 'username':
            if Usuario.query.filter_by(username=campo).first():
                return False
        if tipo == 'email':
            if Usuario.query.filter_by(email=campo).first():
                return False
        return True