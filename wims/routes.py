from wims import app
from flask import render_template, redirect, url_for, flash
from wims.models import user_info
from wims.forms import FormInscription, FormConnexion
from wims import db
from flask_login import login_user


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
            flash(f"Connection réussie sous l'username {passed_user.login_user}", category='success')
            return redirect(url_for('connexion'))
        else:
            flash(f"Erreur, le nom d'utilisateur ne correspond pas au mot de passe !", category='danger')
    return render_template('connexion.html', form=form)
