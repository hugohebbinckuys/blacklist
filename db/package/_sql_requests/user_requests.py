#the goal of the file is to have all requests about user 
#have requests doesn't just mean in string but really run the requests and return the result if it needs one  
from db.package.connexion.connexion import Database

class User_requests :
    def __init__(self):
        self.conexion_instance = Database()
        self.db, self.cursor = self.conexion_instance.get_connexion()

    def insert_new_user (self, tuple_user_info) :
        query = "INSERT INTO user (email, password, job, institution_id) VALUES(%s, %s, %s, %s)"
        try :
            self.cursor.execute(query, tuple_user_info)
            self.db.commit()
            print ("\n--- values sent ---\n")
        except Exception as e : 
            print ("erreur dans la requete d'insertion d'un nouvel user :", e)

    def get_user_information (self, email) :
        request = f"SELECT * FROM user where user.email = '{email}'"
        self.cursor.execute(request)
        response = self.cursor.fetchone()
        return response

    def put_institution_access_to_ok (self, user_email) :
        query = "UPDATE user SET authorized = 1 where email = %s"
        try :
            self.cursor.execute(query, (user_email,))
            self.db.commit()
        except Exception as e : 
            print ("error when trying to update user : ", e)