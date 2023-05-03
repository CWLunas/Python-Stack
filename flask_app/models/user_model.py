from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import listing_model
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$')



class User:
    my_db="pants_schema"
    def __init__(self, data):
        self.id = data['id']
        self.f_name=data['first_name']
        self.l_name=data['last_name']
        self.email=data['email']
        self.password= data['password']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.all_listings= []

    # queries with CRUD and OOP
    @classmethod
    def get_one_user_by_id(cls, data):
        query= '''
            SELECT *
            FROM users
            WHERE users.id = %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return cls(results[0])



    # get all of the users from database, return them as a list of User instances
    @classmethod
    def get_all(cls):
        query='''
            SELECT * FROM users
        '''
        results= connectToMySQL(cls.my_db).query_db(query)

        print(results)
        if results:
            user_objects=[]
            for record in results:
                one_user= cls(record)
                user_objects.append(one_user)
                
            return user_objects
        else:
            return None
    
    # save a user to database
    @classmethod
    def save_user(cls, form_data):
        pw_hash = bcrypt.generate_password_hash(form_data['password'])
        print(pw_hash)
        user_data= {
            'f_name': form_data['f_name'], 
            'l_name': form_data['l_name'],
            'email': form_data['email'],
            'password': pw_hash
        }
        query= '''
                INSERT INTO users
                (first_name, last_name, email, password)
                VALUES
                (%(f_name)s, %(l_name)s, %(email)s, %(password)s);
        '''
        results= connectToMySQL(cls.my_db).query_db(query, user_data)
        
        # the results is returning the id of the record that was just created back to the route that called this method
        return results
    

    # query for a user with all of their listings, return one User instance with a list of Post instances 
    @classmethod
    def get_user_with_listings(cls, data):
        query= '''
            SELECT * FROM users
            LEFT JOIN listings
            ON users.id = listings.user_id
            WHERE users.id = %(user_id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)

        print(results)
        # read your terminal, see if this query worked by adding a print statement. If it doesn't, it will say "something went wrong..." followed by the error 

        # creating a User instance from the database info of the user
        one_user = cls(results[0])
        for row in results:

            # parsing out the database data for tlistings
            listings_data={
                "id" : row['listings.id'], 
                "user_id": row['user_id'],
                "type":row['type'],
                "trend": row['trend'],
                "stoked_val": row['stoked_val'],
                "description": row["description"],
                "created_at": row['listings.created_at'],
                "updated_at": row['listings.updated_at']
            }

            # creating a post instance and appending it to the user's all_post attribute-which is an empty list.
            one_user.all_listings.append(listing_model.Listing(listings_data))

            # return this user to the route in the controller, to be used in the template
        return one_user
    

    # get user by email, in order to check if they exist, if so they can log in
    @classmethod
    def get_user_by_email(cls, data):

        query= '''
            SELECT * FROM users
            WHERE users.email = %(email)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        if results:
            one_user = cls(results[0])
            return one_user
        else:
            return False


    @classmethod
    def get_users_listings(cls):
        query='''
            SELECT * FROM users
            JOIN listings
            ON listings.user_id = users.id
            WHERE users.id= %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query)
        one_user = cls(results[0])
        for row in results:
            listing_data={
                'id': row['listings.id'],
                'user_id':row['user_id'],
                'type':row['type'],
                'trend':row['trend'],
                'description':row['description'],
                'stoked_val':row['stoked_val'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
            }
            one_user.all_listings.append(listing_data)
        return one_user

    @staticmethod
    def validate_register(form_data):
        is_valid= True
        # check if the user exists
        data= { "email": form_data["email"]}
        valid_user = User.get_user_by_email(data)

        # registration validations
        if len(form_data['f_name']) < 2:
            flash("First Name must be atleast 2 characters", "register")
            is_valid= False
        if len(form_data['l_name']) < 2:
            flash("Last Name must be atleast 2 characters", "register")
            is_valid= False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!","register")
            is_valid=False
        if valid_user:
            flash("Email already in use!", "register")
            is_valid=False
        # if not PWORD_REGEX.match(form_data['password']):
        #     flash("Password requires one number and a special character", 'register')
        #     is_valid= False    
        if len(form_data['password']) < 8:
            flash("Password needs to be atleast 8 characters","register")
            is_valid=False
        if form_data['conf_password'] != form_data['password']:
            flash("password and confirm password must match!","register")
            is_valid=False

        return is_valid
        

    @staticmethod
    def validate_login(form_data):
        is_valid= True
        
        data= { "email": form_data["login_email"]}
        valid_user = User.get_user_by_email(data)
        if not valid_user:
            flash('Invalid Crendentials', "login")
            is_valid=False
        if valid_user:
            if not bcrypt.check_password_hash(valid_user.password, form_data['login_password']):
                flash('Invalid Credentials','login')
                is_valid=False
        return is_valid


            
