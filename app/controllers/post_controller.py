from app.models import Post
from app import db
from datetime import datetime

class PostController:
    def novoPost(form, user_obj):
        try:
            post = Post()
            form.populate_obj(post)
            
            post.user = user_obj
            post.user_id = user_obj.id
            
            db.session.add(post)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            print(f'ERRO NA CRIAÇÃO DE POSTAGEM: {e}')
            return False