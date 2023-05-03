from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "heros"
    def __init__(self, data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.heros_liked=[]

    @classmethod
    def save(cls,data):
        query  = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s,%(last_name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_one_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    