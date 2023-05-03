from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model

@app.route('/')
def login_reg():
    return render_template('index.html')

@app.route('/user/register', methods=['POST'])
def register_user():
    if not user_model.User.validate_register(request.form):
        return redirect('/')
    new_user= user_model.User.save_user(request.form)
    print(new_user)
    session['user_id'] = new_user
    return redirect('/listings')

@app.route('/user/login', methods=['POST'])
def login_user():
    if not user_model.User.validate_login(request.form):
        return redirect('/')
    email_data={
        'email':request.form['login_email']
    }
    returning_user= user_model.User.get_user_by_email(email_data)
    session['user_id']= returning_user.id
    return redirect('/listings')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



