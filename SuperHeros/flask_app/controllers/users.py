from flask_app import app
from flask import render_template, jsonify, request, redirect

from flask_app.models import user, hero
import os
print( os.environ.get("FLASK_APP_API_KEY") )

@app.route('/')
def index():
    user= 1
    return redirect(f'/dashboard/{user}')

@app.route('/dashboard/<int:user_id>')
def dashboard(user_id):
    data={
        "id":user_id
    }
    current_user=user.User.get_one_user_by_id(data)
    return render_template('index.html', user=current_user)










