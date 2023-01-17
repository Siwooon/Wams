from wims import app
from flask import render_template, redirect, url_for
from wims.models import user_info
from wims.forms import FormInscription, FormConnexion
from wims import db


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = FormInscription()
    if form.validate_on_submit():
        user_to_create = user_info(login_user=form.username.data,
                                    mail_user = form.mail.data,
                                    password_user = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('connexion'))
    return render_template('inscription.html', form=form)

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    form = FormConnexion()
    if form.validate_on_submit():
        user_to_create = user_info(username=form.username.data,
                                    mail = form.mail.data,
                                    password = form.password.data)
    return render_template('connexion.html', form=form)
