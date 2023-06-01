from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model, post_model


@app.route('/create_post', methods=['POST'])
def create_post():
    new_post = post_model.Post.save_post(request.form)
    return redirect(f'/post/{new_post}')

@app.route('/post/<int:id>')
def view_one_post(id):
    id_data={
        'id': id
    }
    return render_template('one_post.html', one_post = post_model.Post.get_one_post(id_data))

@app.route('/post/edit/<int:id>')
def edit_post(id):
    id_data={
        'id': id
    }
    return render_template('edit_post.html', one_post = post_model.Post.get_one_post(id_data))

@app.route('/update_post', methods=['POST'])
def update_post():
    post_model.Post.update_post(request.form)
    return redirect('/')

@app.route('/post/delete/<int:id>')
def delete_post(id):
    id_data={
        'id': id
    }
    post_model.Post.delete_post(id_data)
    return redirect('/')
