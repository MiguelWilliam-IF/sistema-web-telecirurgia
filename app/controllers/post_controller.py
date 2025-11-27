from app.models import Post
from app import db
import sqlalchemy as sa
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
    
    def listarPosts():
        posts = Post.query.all()
        return posts
    
    def getPostByID(id):
        post = Post.query.get(id)
        return post
    
    def getPostsByUserID(user_id):
        selectStmt = sa.select(Post).where(Post.user_id == user_id)
        result = db.session.execute(selectStmt)
        return result.scalars()
    
    def deletePost(id):
        try:
            post = Post.query.get(id)
            db.session.delete(post)
            db.session.comit()
        except Exception as e:
            db.session.rollback()
            print(f'ERRO NO DELETE DE POST: {e}')