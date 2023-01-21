from wams import db, login_manager
from wams import bcrypt
from flask_login import UserMixin   

class question(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    Label = db.Column(db.String(), nullable =False)
    Etiquette = db.Column(db.String(), nullable =False)
    Question = db.Column(db.String(), nullable =False)
    Réponse1 = db.Column(db.String(), nullable =False)
    Réponse2 = db.Column(db.String(), nullable =False)
    Réponse3 = db.Column(db.String(), nullable =False)
    Réponse4 = db.Column(db.String(), nullable =False)
    bonne_reponse = db.Column(db.String())

    def __repr__(self):
        return f'Question {self.Label}'


class questionnaire(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Label = db.Column(db.String(), nullable =False)
    Q1 = db.Column(db.String(), nullable =False)
    Q2 = db.Column(db.String(), nullable =True)
    Q3 = db.Column(db.String(), nullable =True)
    Q4 = db.Column(db.String(), nullable =True)
    Q5 = db.Column(db.String(), nullable =True)


@login_manager.user_loader
def load_user(id):
    return user_info.query.get(int(id))

class user_info(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String(100), nullable=False)
    mail_user = db.Column(db.String(100), nullable=False)
    password_user = db.Column(db.String(100), nullable=False)
    prof_user = db.Column(db.Integer)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_user = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, passed_password):
        return bcrypt.check_password_hash(self.password_user, passed_password)
