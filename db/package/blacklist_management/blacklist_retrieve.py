from flask import Blueprint
from db.package._sql_requests.blacklist_requests import Blacklist_requests

#creation d'un blueprint 
blacklist_retrieve_bp = Blueprint("blacklist_retrieve_bp", __name__)

@blacklist_retrieve_bp.route("/retrieve_blacklisted", methods=["GET"])
def retrieve () : 
    blacklist_requests_instance = Blacklist_requests()

    result = blacklist_requests_instance.retrieve_blacklisted()
    return {"blacklisted":result}



# continuer a mettre tout python sous classes la pour les fichiers suivants. 