# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_db'

from flask_app.models import model_ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']

    @property
    def ninjas(self):
        return model_ninja.Ninja.get_all_of_dojo({'dojo_id': self.id})

    #C
    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    #R
    @classmethod
    def get_one(cls, data:dict) ->list:
        query = "SELECT * from dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_all(cls) ->list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_dojos = []
            for dojo in results:
                all_dojos.append(cls(dojo))
            return all_dojos
        return False


    #U
    @classmethod
    def update_one(cls, data:dict) ->None:
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)



    #D
    @classmethod
    def delete_one(cls, data:dict) ->None:
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)