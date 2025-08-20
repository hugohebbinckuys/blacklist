#the goal of the file is to have all requests about user 
#have requests doesn't just mean in string but really run the requests and return the result if it needs one  

from db.package.connexion.connexion import db, cursor

def insert_new_user (tuple_user_info) :
    query = "INSERT INTO user (email, password, job, institution_id) VALUES(%s, %s, %s, %s)"
    try :
        cursor.execute(query, tuple_user_info)
        db.commit()
        print ("\n--- values sent ---\n")
    except Exception as e : 
        print ("erreur dans la requete d'insertion d'un nouvel user :", e)

def get_user_information (email) :
    request = f"SELECT * FROM user where user.email = '{email}'"
    cursor.execute(request)
    response = cursor.fetchone()
    return response