from flask_app.config.mysqlconnection import connectToMySQL


class Ninja: 
    DB = "Dojos_and_Ninjas"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.dojo_id = db_data['dojo_id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL(cls.DB).query_db(query)
        ninjas =[]
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        one_row = connectToMySQL(cls.DB).query_db(query,data)
        return cls(one_row[0])


    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
    #on an update we need to always USE A WHERE CLAUSE so that the entire database doesnt update


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)
