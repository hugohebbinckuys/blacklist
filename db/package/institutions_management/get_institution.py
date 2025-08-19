from db.package.connexion.connexion import db, cursor
from db.package.utils.db_requests.get_requests import get_institution_by_id_request

def get_institution_by_id (id) :
    request = get_institution_by_id_request(id)
    cursor.execute(request)
    response = cursor.fetchone()
    return response