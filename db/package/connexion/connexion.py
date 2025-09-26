import mysql, mysql.connector

class Database: 
    def __init__(self):
        self.host="mysql-blacklist-db.alwaysdata.net"
        self.user="425889_hh"
        self.password=".jkEqv@wQe2976U"
        self.database="blacklist-db_01" 
        self.db = None 
        self.cursor = None

    def get_connexion(self) : 
        try :
            db = mysql.connector.connect(
                host="mysql-blacklist-db.alwaysdata.net", 
                user="425889_hh",
                password=".jkEqv@wQe2976U",
                database="blacklist-db_01"
            )
            cursor = db.cursor()
            print ("\n--- connected to the db ---\n")
            self.db = db 
            self.cursor = cursor

            return self.db, self.cursor

        except Exception as e : 
            print("\n--- error when trying to connect to the database ---\n", e)
            return None, None
        
    def close_conexion (self) : 
        if self.cursor : 
            self.cursor.close()
        if self.db : 
            self.db.close()
        print ("--conexion closed--")

# if __name__ == "__main__" : 
#     database = Database()
#     database.get_connexion()