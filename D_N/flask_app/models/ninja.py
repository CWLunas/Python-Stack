from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (dojos_id, first_name, last_name, age) VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        result = connectToMySQL('dojo_ninjas_schema').query_db(query,data)
        return result
