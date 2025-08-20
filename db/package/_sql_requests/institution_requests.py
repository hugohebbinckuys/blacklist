#the goal of the file is to have all requests about institutions 
#have requests doesn't just mean in string but really run the requests and return the result if it needs one

from db.package.connexion.connexion import db, cursor

def get_institution_by_id (id) :
    request = f"SELECT password from institution where institution.id = '{id}'"
    cursor.execute(request)
    response = cursor.fetchone()
    return response

def get_all_institutions_request () : 
    request = "SELECT * from institution"
    cursor.execute(request)
    response = cursor.fetchall()
    return response