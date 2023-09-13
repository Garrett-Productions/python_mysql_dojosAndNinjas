from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = "Dojos_and_Ninjas"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.list_of_ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        database = connectToMySQL(cls.DB).query_db(query)
        dojo_list = []
        print("look here amigo", dojo_list)
        for each_dojo in database:
            dojo_list.append(cls(each_dojo))
        return dojo_list

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" #ninjas.id
        results = connectToMySQL('Dojos_and_Ninjas').query_db(query, data)
        print("My results are here", results)
        #The results returns a row from the Database
        dojo = cls(results[0])
        print("This is where my 0 results are", results[0])
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            each_ninja = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db["dojo_id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"] #for the ambiguous values you need to specify which table it belongs to.
            }
            dojo.list_of_ninjas.append(ninja.Ninja(each_ninja)) #document, class, parsed data
        return dojo