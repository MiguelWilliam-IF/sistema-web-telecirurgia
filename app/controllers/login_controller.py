from app.models import Usuario
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

class LoginController:
    def login(form):
        email = form.email.data.strip()
        user = Usuario.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return True
        else:
            return False
        
    def logout():
        return logout_user()