from flask import request, Blueprint
import bcrypt
from db.package._sql_requests.institution_requests import Institution_requests
# from db.package._sql_requests.user_requests import put_institution_access_to_ok, get_user_information
from db.package._sql_requests.user_requests import User_requests

#crea d'un bleupriunt avant 
institution_login_bp = Blueprint("institution_login_bp", __name__)

@institution_login_bp.route("/institution_login", methods=["POST"])
def institution_login () : 
    institution_requests_instance = Institution_requests()
    sent = request.json
    email = sent.get("user_email")
    password_entered = sent.get("password_entered")
    institution_id = sent.get("institution_id")
    print (password_entered)
    print (institution_id)
    institution_password = institution_requests_instance.get_institution_by_id(institution_id)
    print (institution_password)

    if (bcrypt.checkpw(password_entered.encode('utf-8'), institution_password[0].encode('utf-8'))) :
        # mettre à 1 le authorized sur la bdd 
        user_requests_instance = User_requests()
        update_result = user_requests_instance.put_institution_access_to_ok(email)
        print (update_result)
        user = user_requests_instance.get_user_information(email)
        print("user : ", user)
        return {"status": "OK", "user_updated":user, "redirect":"connected/menu"}
    else : 
        return {"status":"KO", "redirect":"institution_auth"}
