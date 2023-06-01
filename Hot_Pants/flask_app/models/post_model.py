from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
class Post:
    my_db="blog_schema"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title= data['title']
        self.content = data['content']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def save_post(cls, data):
        query='''
            INSERT INTO posts(user_id, title, content)
            VALUES(%(user_id)s, %(title)s, %(content)s);
        '''
        return connectToMySQL(cls.my_db).query_db(query, data)

    @classmethod
    def get_one_post(cls, data):
        query='''
            SELECT * FROM posts
            WHERE posts.id = %(id)s
            '''
        results= connectToMySQL(cls.my_db).query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def update_post(cls,data):
        query='''
            UPDATE posts
            SET title=%(title)s, content=%(content)s
            WHERE posts.id= %(id)s
        '''
        results = connectToMySQL(cls.my_db).query_db(query, data)

        return results

    @classmethod
    def delete_post(cls, data):
        query= '''
            DELETE FROM posts
            WHERE posts.id=%(id)s;
        '''
        return connectToMySQL(cls.my_db).query_db(query, data)
    