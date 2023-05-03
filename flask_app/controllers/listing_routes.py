from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import listing_model, user_model

@app.route('/listings')
def user_dash():
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': session['user_id']
    }
    one_user= user_model.User.get_one_user_by_id(id_data)
    all_listings= listing_model.Listing.get_all_listings()
    return render_template('view_all.html', user=one_user, all_listings=all_listings )

@app.route('/listings/new')
def create_form():
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': session['user_id']
    }
    one_user= user_model.User.get_one_user_by_id(id_data)
    return render_template('create_form.html', user=one_user)

@app.route('/listings/edit/<int:id>')
def edit_form(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }
    one_listing= listing_model.Listing.get_one_listing_w_user(id_data)
    return render_template('edit_form.html', listing=one_listing)

@app.route('/listings/user/<int:id>')
def view_user_listings(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'user_id': id
    }
    one_user= user_model.User.get_user_with_listings(id_data)
    return render_template('view_user_listings.html',user= one_user)

#view one
@app.route('/listings/<int:id>')
def view_one(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }
    one_listing= listing_model.Listing.get_one_listing_w_user(id_data)
    user_data={
        'id': session['user_id']
    }
    one_user= user_model.User.get_one_user_by_id(user_data)
    return render_template('view_one.html', listing=one_listing, user=one_user)

#create/POST w/ validation
@app.route('/listings/create', methods=['POST'])
def create_listing():
    if 'user_id' not in session: 
        return redirect('/')
    if not listing_model.Listing.validate_listing(request.form):
        return redirect('/listings/new')
    listing_data={
        'user_id': session['user_id'],
        'type': request.form['type'],
        'trend':request.form['trend'],
        'description':request.form['description']

    }
    listing_model.Listing.save_listing(listing_data)
    id_data={
        'id': session['user_id']
    }
    one_user= user_model.User.get_one_user_by_id(id_data)
    return redirect(f'/listings/user/{one_user.id}')




#update/POST w/ validation
@app.route('/listings/update/<int:id>', methods=['POST'])
def update_listing(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }
    one_listing= listing_model.Listing.get_one_listing_w_user(id_data)

    if not listing_model.Listing.validate_listing(request.form):
        return redirect(f'/listings/edit/{one_listing.id}')
    
    else:
        listing_model.Listing.update_listing(id_data)
        return redirect(f'/listings/{one_listing.id}')

#delete
@app.route('/listings/delete/<int:id>')
def delete_listing(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }

    pass

#coolit/deduct 1 from stoke_val
@app.route('/listings/cool_it/<int:id>')
def cool_it(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }
    one_listing= listing_model.Listing.get_one_listing_w_user(id_data)
    stoked_val= int(one_listing.stoked_val)
    stoked_val-= 1
    stoke_data={
        'stoked_val': stoked_val,
        'id': id
    }
    listing_model.Listing.update_stoked_val(stoke_data)
    return redirect(f'/listings/{one_listing.id}')


#stokeit/add 1 to stoke_val
@app.route('/listings/stoke_it/<int:id>')
def stoke_it(id):
    if 'user_id' not in session: 
        return redirect('/')
    id_data={
        'id': id
    }
    one_listing= listing_model.Listing.get_one_listing_w_user(id_data)
    stoked_val= int(one_listing.stoked_val)
    stoked_val+= 1
    stoke_data={
        'stoked_val': stoked_val,
        'id': id
    }
    listing_model.Listing.update_stoked_val(stoke_data)
    return redirect(f'/listings/{one_listing.id}')