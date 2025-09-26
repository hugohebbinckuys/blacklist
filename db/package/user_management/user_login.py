from flask import request, Blueprint
from flask_bcrypt import bcrypt
from db.package._sql_requests.user_requests import User_requests

user_login_bp = Blueprint("user_login_bp", __name__)

@user_login_bp.route("/login", methods=["POST"])
def login () : 
    user_requests_instance = User_requests()
    sent = request.json
    email = sent.get("email")
    password = sent.get("password")
    # institution = sent.get("institution")
    print ("informations reçues : ", email, password)

    user_information = user_requests_instance.get_user_information(email)

    if (user_information != None) :    
        if (bcrypt.checkpw(password.encode('utf-8'), user_information[1].encode('utf-8'))) :
            return {'authorized' : True, "user_info" : user_information}
        else : 
            return {'authorized': False, 'password': 'NOT ok'}
    else : 
        print ("user '"+email+"' inexistant")
        return {'authorized': False, 'user': 'NOT exists'}