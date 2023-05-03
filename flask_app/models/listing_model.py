from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash

class Listing:
    my_db="pants_schema"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.type = data['type']
        self.trend= data['trend']
        self.description= data['description']
        self.stoked_val= data['stoked_val']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.creator=None

    # crud queries 

    # insert into
    @classmethod
    def save_listing(cls,data):
        query='''
            INSERT INTO listings(user_id, type, trend, description)
            VALUES(%(user_id)s, %(type)s, %(trend)s, %(description)s);
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return results


    # select w/join (read all and read one)
    @classmethod
    def get_all_listings(cls):
        query='''
            SELECT * FROM listings
            JOIN users
            ON listings.user_id = users.id;
        '''
        results= connectToMySQL(cls.my_db).query_db(query)
        if results:
            all_listings=[]
            for row in results:
                one_listing=cls(row)

                user_data={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': ' ',
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                one_listing.creator= user_model.User(user_data)
                all_listings.append(one_listing)
            return all_listings
        else:
            return []

    @classmethod
    def get_one_listing_w_user(cls,data):
        query='''
            SELECT * FROM listings
            JOIN users
            ON listings.user_id = users.id
            WHERE listings.id= %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query,data)
        one_listing = cls(results[0])
        for row in results:
            user_data={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': ' ',
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
            one_listing.creator= user_model.User(user_data)
        return one_listing

    #update
    @classmethod
    def update_listing(cls,data):
        query='''
            UPDATE listings SET type=%(type)s, trend=%(trend)s, description= %(description)s) WHERE listings.id = %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return results


    #delete
    @classmethod
    def delete_listing(cls,data):
        query='''
            DELETE FROM listings WHERE listings.id = %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return results
    
    @classmethod
    def update_stoked_val(cls, data):
        query='''
        UPDATE listings SET stoked_val=%(stoked_val)s
        WHERE listings.id = %(id)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return results
    
    @staticmethod
    def validate_listing(data):
        is_valid= True
        if len(data['type']) < 3:
            flash("Type must be atleast 3 characters", 'listing')
            is_valid=False
        if len(data['trend']) < 3:
            flash("Trend must be atleast 3 characters",'listing')
            is_valid=False
        if len(data['description']) < 5:
            flash("Description must be atleast 5 characters",'listing')
            is_valid=False
        return is_valid