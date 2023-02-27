from wams import app
from flask import render_template, redirect, url_for, jsonify, flash, request, json
from wams.db import db
from wams.db import question, user_info, Etiquettes, questionnaire
from wams.forms import Form, FormInscription, FormConnexion
import os
import csv
import random, string

from flask_login import login_user, logout_user

globalTags=[]
roomOuvertes=[]

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

globalTags=["Web", "Java", "Arithmétique", "Graphes"]
engine = create_engine('sqlite:///instance/wams.db?check_same_thread=False')
connection = engine.connect()
print(engine.table_names())
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()
questionnaireTable = Table("questionnaire", metadata, autoload=True, autoload_with=engine)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/pagesQuestion', methods=['GET', 'POST'])
def pagesQuestion():
    return render_template('pagesQuestion.html', questions=question.query.all(), globalTags=globalTags, len=len(globalTags), len9 = len(globalTags) if len(globalTags)<9 else 9)# listeTags = listeTags, lenTags = len(listeTags))

@app.route('/pagesQuestionWaitingRoom', methods=['GET', 'POST'])
def pagesQuestionWaitingRoom():
    listeTags = json.loads(request.data)["listeTags"]
    strTags = json.loads(request.data)["strTags"]
    return render_template("pagesQuestion.html", questions=question.query.all(), globalTags=globalTags, len=len(globalTags), len9=len(globalTags) if len(globalTags)<9 else 9, listeTags=listeTags, strTags=strTags)

isChecked = False

@app.route('/oneAnswer', methods=['GET', 'POST'])
def oneAnswer():
    global isChecked
    isChecked = not(isChecked)
    return redirect(url_for('editeur'))


@app.route('/editeur', methods=['GET', 'POST'])
def editeur():
    for tag in Etiquettes.query.all():
        if not(tag.id in globalTags): #Initialise les étiquettes de base
            globalTags.append(tag.id)
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
        bonne_reponse = form.bonne_reponse.data
        
        listNewTags = Etiquette.split(",")
        for i in range(len(listNewTags)) :
            if not bool(Etiquettes.query.filter_by(id=listNewTags[i]).first()):
                if not (listNewTags[i] == ""): #Ajout des étiquettes submit à la db sans doublon
                    newTag = Etiquettes(id=listNewTags[i])
                    db.session.add(newTag)
                    db.session.commit()
                
        for tag in Etiquettes.query.all():
            if not bool(Etiquettes.query.filter_by(id=tag.id).first()):
                if not (tag.id == ""): #Ajout des nouvelles étiquettes de la db dans une liste envoyée au html
                    globalTags.append(tag.id)
        print("PIOUPIOU", isChecked)
        
        if not(isChecked):
            print("erreur", isChecked)
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
            Questionfilter.bonne_reponse = bonne_reponse
        else:
            QuestionToAdd = question(Label=Label, Etiquette=Etiquette, Question=Questiondata, Réponse1=Réponse1, Réponse2=Réponse2, Réponse3=Réponse3, Réponse4=Réponse4, bonne_reponse=bonne_reponse)
            db.session.add(QuestionToAdd)
            db.session.commit()
            return redirect(url_for('editeur'))
        db.session.commit()
    
    
    return render_template('editeur.html', form = form, question = AllQuestion, globalTags=globalTags, len=len(globalTags), len9 = len(globalTags) if len(globalTags)<9 else 9)

@app.route('/waitingRoom', methods=['GET', 'POST'])
def waitingRoom():
    return render_template('waitingRoom.html')

@app.route('/diffusionQ/<codeRoom>', methods=['GET', 'POST'])
def diffusionQ(codeRoom):
    return render_template('diffusionQuestion.html', codeRoom=codeRoom)

@app.route('/updateDiffusionQuestion', methods=['GET', 'POST'])
def updateDiffusionQuestion():
    codeRoomA = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    codeRoom = codeRoomA if codeRoomA not in roomOuvertes else updateDiffusionQuestion()
    roomOuvertes.append(codeRoom)
    return redirect(url_for('diffusionQ', codeRoom=codeRoom))

@app.route('/update/<int:id>', methods=['GET'])
def update(id):
    Question = question.query.get(id)
    return jsonify(Label=Question.Label, 
                   Etiquette=Question.Etiquette, 
                   Question=Question.Question, 
                   Réponse1=Question.Réponse1,
                   Réponse2=Question.Réponse2,
                   Réponse3=Question.Réponse3,
                   Réponse4=Question.Réponse4,
                   bonne_reponse=Question.bonne_reponse)

@app.route('/add', methods=['POST'])
def addQuestion():
    listeQuestions = request.get_json()['listeQuestions']
    x = len(questionnaireTable.columns)-2
    print(listeQuestions)
    print(len(listeQuestions))
    nbcolonnes = len(questionnaireTable.columns) - 2
    print(nbcolonnes)
    
    while len(listeQuestions) > nbcolonnes:
        x +=1
        Column_name = f'Q{x}'

        print(Column_name)
        query = f'ALTER TABLE questionnaire ADD {Column_name};'
        connection.execute(query)
        nbcolonnes +=1
    
    # name_columns = [col.name for col in questionnaireTable.columns]
    new_questionnaire = questionnaire(Label=listeQuestions[0])
    listeQuestions.pop(0)
    for i in range(len(listeQuestions)):
        setattr(new_questionnaire, f"Q{str(i+1)}", listeQuestions[i])
    db.session.add(new_questionnaire)
    db.session.commit()
    return redirect(url_for('editeur'))

@app.route('/q/<id>', methods=['POST', 'GET'])
def q(id):
    allQuestionnaire = questionnaire.query.all()
    
    ligne_selectionnée = db.session.query(questionnaire).filter_by(Label=id).first()
    print(ligne_selectionnée)
    labels = []
    sto = len(ligne_selectionnée.__table__.columns)
    print(sto)
    for i in range(1, len(ligne_selectionnée.__table__.columns)-2):
        column = f"Q{i}"
        value = getattr(ligne_selectionnée, column)
        if value:
            labels.append(value)
    questionsRows = db.session.query(question).filter(question.Label.in_(labels)).all()

    idQuestions = []
    labelQuestions = []
    for questionRow in questionsRows:
        idQuestions.append(questionRow.id)
        labelQuestions.append(questionRow.Label)
    print(idQuestions)
    


    return render_template('questionnaire.html', idQuestions = idQuestions, labelQuestions= labelQuestions)


@app.route('/quest/<int:id>', methods=['POST', 'GET'])
def quest(id):
    Question = question.query.get(id)
    bonnesReps = question.query.with_entities(question.bonne_reponse)
    bonneRep = str(bonnesReps[id-1]).strip("()',").replace("\\n", "\n").replace("\\r", "")
    print(bonneRep)

    reponse = request.form.get('reponses')
    print(reponse)
    if reponse == bonneRep:
        flash("Bonne réponse !", category='success')
    elif (request.form.get('reponses') == None) :
        # flash("Veuillez répondre à la question", category='danger')
        None

    else:
        flash("Mauvaise réponse !", category='danger')
    return render_template('question.html', Label=Question.Label, 
                   Etiquette=Question.Etiquette, 
                   Question=Question.Question, 
                   Réponse1=Question.Réponse1,
                   Réponse2=Question.Réponse2,
                   Réponse3=Question.Réponse3,
                   Réponse4=Question.Réponse4)
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = FormInscription()
    if form.validate_on_submit():
        user_to_create = user_info(login_user=form.username.data,
                                    mail_user = form.mail.data,
                                    password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('connexion'))
    if form.errors != {}:
        for errors in form.errors.values():
            flash(f'Erreur : {errors}', category='danger')
    return render_template('inscription.html', form=form)

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    form = FormConnexion()
    if form.validate_on_submit():
        passed_user = user_info.query.filter_by(login_user=form.username.data).first()
        if passed_user and passed_user.check_password_correction(passed_password = form.password.data):
            login_user(passed_user)
            # flash(f"Connection réussie sous l'username {passed_user.login_user}", category='success')
            return redirect(url_for('editeur'))
        else:
            flash(f"Erreur, le nom d'utilisateur ne correspond pas au mot de passe !", category='danger')
    return render_template('connexion.html', form=form)

@app.route('/deconnexion', methods=['GET', 'POST'])
def deconnexion():
    logout_user()
    flash("Deconnexion réussie !", category='info')
    return redirect(url_for('editeur'))

@app.route('/creerAllComptes', methods=["GET", "POST"])
def creerAllComptes():
    form = FormInscription()
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for data in csv_file:
                    print(data)
                    user_to_create = user_info(login_user=f"{data[0]}{data[1]}",
                                                mail_user = "",
                                                password = data[2])
                    db.session.add(user_to_create)
                    db.session.commit()
    return render_template('creerAllComptes.html')

app.config['FILE_UPLOADS'] = "C:\\Users\\user\\Desktop\\Travail\\L2_info_FDS\\Semestre 4\\perso\\projProg\\wams\\uploads"
