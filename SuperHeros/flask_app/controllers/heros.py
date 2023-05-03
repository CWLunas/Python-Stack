from flask_app.models import user, hero
from flask_app import app
import requests
from flask import render_template, jsonify, request, redirect
import os
os.environ.get("FLASK_API_KEY")

@app.route('/searching', methods=['POST'])
def searching():
    r= requests.get(f'https://superheroapi.com/api/{os.environ.get("FLASK_API_KEY")}/search/{request.form["name"]}')
    return jsonify(r.json())

@app.route('/dashboard/<int:user_id>/<int:hero_id>')
def join_hero_to_user(user_id, hero_id):
    
    pass






