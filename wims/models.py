from wims import db, login_manager
from wims import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id_user):
    return user_info.query.get(int(user_id_user))

class user_info(db.Model, UserMixin):
    id_user = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String(100), nullable=False)
    mail_user = db.Column(db.String(100), nullable=False)
    password_user = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_user = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, passed_password):
        return bcrypt.check_password_hash(self.password_user, passed_password)