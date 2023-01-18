from wams import app
from flask import render_template, redirect, url_for, jsonify
from wams.db import question
from wams.forms import Form
from wams.db import db


@app.route('/', methods=['GET', 'POST'])
def home():
    AllQuestion = question.query.all()
    form = Form()
    if form.validate_on_submit():

        Label = form.Label.data
        Etiquette = form.Etiquette.data
        Questiondata = form.Question.data
        Réponse1 = form.Réponse1.data
        Réponse2 = form.Réponse2.data
        Réponse3 =form.Réponse3.data
        Réponse4 = form.Réponse4.data

        if not Label.strip() or not Etiquette.strip() or not Questiondata.strip() or not Réponse1.strip() or not Réponse2.strip() or not Réponse3.strip() or not Réponse4.strip():
            raise ValueError("Les champs ne peuvent pas être vides ou remplis d'espaces uniquement.")

        Questionfilter = question.query.filter_by(Label=Label).first()

        if Questionfilter:
            Questionfilter.Etiquette = Etiquette
            Questionfilter.Question = Questiondata
            Questionfilter.Réponse1 = Réponse1
            Questionfilter.Réponse2 = Réponse2
            Questionfilter.Réponse3 = Réponse3
            Questionfilter.Réponse4 = Réponse4
        else:
            QuestionToAdd = question(Label=Label, Etiquette=Etiquette, Question=Questiondata, Réponse1=Réponse1, Réponse2=Réponse2, Réponse3=Réponse3, Réponse4=Réponse4)
            db.session.add(QuestionToAdd)
            db.session.commit()
            return redirect(url_for('home'))
        db.session.commit()
    
    
    return render_template('home.html', form = form, question = AllQuestion)


@app.route('/update/<int:id>', methods=['GET'])
def update(id):
    Question = question.query.get(id)
    return jsonify(Label=Question.Label, 
                   Etiquette=Question.Etiquette, 
                   Question=Question.Question, 
                   Réponse1=Question.Réponse1,
                   Réponse2=Question.Réponse2,
                   Réponse3=Question.Réponse3,
                   Réponse4=Question.Réponse4)



