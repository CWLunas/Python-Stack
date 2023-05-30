from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def get_all():
    dojos = Dojo.get_all()
    print('Dojo')
    return render_template('index.html', all_dojos=dojos())



@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one(data))

@app.route('/dojo/edit/<int:id>')
def edit_dojo(id):
    data = {
        'id':id
    }
    return render_template('dojo.html', dojo=Dojo.get_one(data))

@app.route('/dojos/delete/<int:id>')
def delete_dojo(id):
    data = {
        'id':id
    }
    Dojo.delete(data)
    return redirect('/dojos')


@app.route('/dojos/update',methods=['POST'])
def update_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect(f'/dojos/show/dojo_id')