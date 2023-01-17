from wims import db
class user_info(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    login_user = db.Column(db.String(100), nullable=False)
    mail_user = db.Column(db.String(100), nullable=False)
    password_user = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Nom {self.login_user}"