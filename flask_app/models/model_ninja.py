# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_db'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']


    #C
    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    #R
    @classmethod
    def get_one(cls, data:dict) ->list:
        query = "SELECT * from ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_all(cls) ->list:
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_ninjas = []
            for ninja in results:
                all_ninjas.append(cls(ninja))
            return all_ninjas
        return False

    @classmethod
    def get_all_of_dojo(cls, data) ->list:
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_ninjas = []
            for ninja in results:
                all_ninjas.append(cls(ninja))
            return all_ninjas
        return False
    
    @classmethod
    def get_dojo(cls, data:dict) ->list:
        query = "SELECT dojos.name FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;" 
        band_name = connectToMySQL(DATABASE).query_db(query)
        return dojo_name



    #U
    @classmethod
    def update_one(cls, data:dict) ->None:
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)



    #D
    @classmethod
    def delete_one(cls, data:dict) ->None:
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)