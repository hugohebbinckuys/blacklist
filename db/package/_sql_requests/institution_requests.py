#the goal of the file is to have all requests about institutions 
#have requests doesn't just mean in string but really run the requests and return the result if it needs one

# from db.package.connexion.connexion import db, cursor
from db.package.connexion.connexion import Database

class Institution_requests :
    def __init__(self):
        self.conexion_instance = Database()
        self.db, self.cursor = self.conexion_instance.get_connexion()

    def get_institution_by_id (self, id) :
        query = f"SELECT password from institution where institution.id = '{id}'"
        self.cursor.execute(query)
        response = self.cursor.fetchone()
        return response

    def get_all_institutions_request (self) : 
        query = "SELECT * from institution"
        self.cursor.execute(query)
        response = self.cursor.fetchall()
        return response
    