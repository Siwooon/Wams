from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length

class FormInscription(FlaskForm):
    username = StringField(label="Username:", validators=Length(min=2, max=12))
    mail = StringField(label="Adresse mail:")
    password1 = StringField(label="Mot de passe:", validators=Length(min=8))
    password2 = StringField(label="Confirmer mot de passe:")
    submit = SubmitField(label="submit")
  
class FormConnexion(FlaskForm):
    username = StringField(label="username")
    mail = StringField(label="mail")
    password = StringField(label="password")
    submit = SubmitField(label="submit")
  