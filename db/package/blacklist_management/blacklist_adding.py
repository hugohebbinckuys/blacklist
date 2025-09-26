from flask import Blueprint, request
from db.package._sql_requests.blacklist_requests import Blacklist_requests

blacklist_adding_bp = Blueprint("blacklist_adding_bp", __name__)

@blacklist_adding_bp.route("/new_blacklisted", methods=["POST"])
def blacklisted_addition () : 
    blacklist_requests_instance = Blacklist_requests() 

    sent = request.json
    blacklisted_information = (sent.get("nom"), sent.get("prenom"), sent.get("numero"), sent.get("email"), sent.get("description"), sent.get("institution_id"))
    result = blacklist_requests_instance.insert_new_blacklisted(blacklisted_information)

    return result