from flask_app.config.mysqlconnection import connectToMySQL

class Hero:
    db = "heros"
    def __init__(self, data):
        # we will save the api's id for the hero as the id for the table in our database
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query  = "INSERT INTO heros (id,name) VALUES (%(id)s, %(name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_one_hero(cls,data):
        query = "SELECT * FROM heros WHERE name = %(name)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_all__heros_json(cls):
        query = "SELECT * FROM heros;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        hero_list=[]
        for row in results:
            hero_list.append(Hero(row))

        return hero_list