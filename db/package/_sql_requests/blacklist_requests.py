# from db.package.connexion.connexion import db, cursor

from db.package.connexion.connexion import Database

class Blacklist_requests :
    def __init__(self):
        self.conexion_instance = Database()
        self.db, self.cursor = self.conexion_instance.get_connexion()

    def retrieve_blacklisted (self) : 
        self.db, self.cursor = self.conexion_instance.get_connexion()
        query = "Select * from blacklist"
        try :
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print("\n Here is the result of all blacklisted :", result)
            return result
        except Exception as e : 
            print ("Error when retrieving blacklisted : ", e)
            return []
        
    def insert_new_blacklisted (self, blacklisted_information) : 
        self.db, self.cursor = self.conexion_instance.get_connexion()
        query = "insert into blacklist (name, first_name, phone_number, email, description, institution_id) values (%s, %s, %s, %s, %s, %s)"
        print ("\n", blacklisted_information, "\n")
        try :
            self.cursor.execute(query, blacklisted_information)
            self.db.commit()
            return {"status":"success", "blacklisted":"sent"}
        except Exception as e : 
            print ("error when trying to add a blacklisted : ", e)
            return {"status":"error", "blacklisted":"not sent"}