from wams import db


class question(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    Label = db.Column(db.String(), nullable =False)
    Etiquette = db.Column(db.String(), nullable =False)
    Question = db.Column(db.String(), nullable =False)
    Réponse1 = db.Column(db.String(), nullable =False)
    Réponse2 = db.Column(db.String(), nullable =False)
    Réponse3 = db.Column(db.String(), nullable =False)
    Réponse4 = db.Column(db.String(), nullable =False)

    def __repr__(self):
        return f'Question {self.Label}'