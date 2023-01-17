from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Form(FlaskForm):
    Label = StringField(label='Label')
    Etiquette = StringField(label='Etiquette')
    Question = StringField(label='Question ')
    Réponse1 = StringField(label='Réponse 1')
    Réponse2 = StringField(label='Réponse 2')
    Réponse3 = StringField(label='Réponse 3')
    Réponse4 = StringField(label='Réponse 4')

    submit = SubmitField(label='Envoyer')

