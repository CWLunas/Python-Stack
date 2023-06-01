from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model

@app.route('/')
def user_with_blogs():
    return render_template('user_w_blogs.html', one_user= user_model.User.get_user_with_posts())

@app.route('/users/new')
def add_users():
    return render_template('user_form.html')

@app.route('/process_user', methods=['POST'])
def save_user():
    user_model.User.save_user(request.form)
    return redirect('/users')

