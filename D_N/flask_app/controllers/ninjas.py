from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html',dojos= dojo.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja(id):
    data ={ 
        "id":id
    }
    ninja.Ninja.save(request.form)
    return redirect('/dojos/<int:id>')

@app.route('/user/edit/<int:id>')
def edit_ninja(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",ninja.Ninja.get_one(data))

@app.route('/ninja/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    ninja.Ninja.delete(data)
    return redirect('/dojos')

@app.route('/ninjas/update',methods=['POST'])
def update():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["email"]
    }
    ninjas_id = ninja.Ninja.save(data)
    return redirect(f'/ninja/show/{ninjas_id}')

