from db.package._sql_requests.institution_requests import Institution_requests
from flask import Blueprint

#crea d'un bleupriunt avant 
institution_send_all_bp = Blueprint("institution_send_all_bp", __name__)

@institution_send_all_bp.route("/recup_institutions", methods=["GET"])
def send_institutions_to_vuejs () :
    institution_requests_instance = Institution_requests()
    institutions = institution_requests_instance.get_all_institutions_request()
    return {"institutions" : institutions, "format de reponse :" : "[(id, 'name', 'location', 'password')]"}