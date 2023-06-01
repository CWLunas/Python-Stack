from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import post_model


class User:
    my_db="blog_schema"
    def __init__(self, data):
        self.id = data['id']
        self.f_name=data['first_name']
        self.l_name=data['last_name']
        self.email=data['email']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.all_posts = []

    # queries with CRUD and OOP

    # get all of the users from database, return them as a list of User instances
    @classmethod
    def get_all(cls):
        query='''
            SELECT * FROM users;
        '''
        results= connectToMySQL(cls.my_db).query_db(query)

        print(results)

        user_objects=[]
        for record in results:
            one_user= cls(record)
            user_objects.append(one_user)
            
        return user_objects
    
    # save a user to database
    @classmethod
    def save_user(cls, form_data):
        query= '''
                INSERT INTO users
                (first_name, last_name, email)
                VALUES
                (%(f_name)s, %(l_name)s, %(email)s);
        '''
        results= connectToMySQL(cls.my_db).query_db(query, form_data)
        
        # the results is returning the id of the record that was just created back to the route that called this method
        return results
    

    # query for a user with all of their posts, return one User instance with a list of Post instances 
    @classmethod
    def get_user_with_posts(cls):
        query= '''
            SELECT * FROM users
            LEFT JOIN posts
            ON users.id = posts.user_id
            WHERE users.id = 1
        '''
        results= connectToMySQL(cls.my_db).query_db(query)

        print(results)
        # read your terminal, see if this query worked by adding a print statement. If it doesn't, it will say "something went wrong..." followed by the error 

        # creating a User instance from the database info of the user
        one_user = cls(results[0])
        for row in results:

            # parsing out the database data for the post
            post_data={
                "id" : row['posts.id'], 
                "user_id": row['user_id'],
                "title":row['title'],
                "content": row['content'],
                "created_at": row['posts.created_at'],
                "updated_at": row['posts.updated_at']
            }

            # creating a post instance and appending it to the user's all_post attribute-which is an empty list.
            one_user.all_posts.append(post_model.Post(post_data))

            # return this user to the route in the controller, to be used in the template
        return one_user



            

