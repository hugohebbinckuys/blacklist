from flask import request, Blueprint # objet fourin par flask pour récupérer les données de la reuqste http recue par le serveur flask (les headers, le contenu etc.)
from db.package.utils.utils import password_hacher
from db.package._sql_requests.user_requests import User_requests

user_creation_bp = Blueprint("user_creation_bp", __name__)

@user_creation_bp.route("/new_user", methods=["POST"])
def new_user () : 
    user_requests_instance = User_requests()
    sent = request.json 
    user = (sent.get("email"), password_hacher(sent.get("password")), sent.get("job"), sent.get("institution"))
    try : 
        user_requests_instance.insert_new_user(user)
        
        authorized_request = user_requests_instance.get_user_information(user[0])
        print ("\n athorized_request for : ", authorized_request)
        authorized = authorized_request[4]
        print ("\n athorized : ", authorized)
        
        if (authorized == 1) :
            return {"status":"OK", "redirect":"connected", "user_info":authorized_request}
        else : 
            return {"status":"OK", "redirect":"institution_auth", "user_info":authorized_request}

    except Exception as e: 
        print ("\n--- Values didn't arrived to the db ---\n")
        print (e)

        return {"status":"KO", "redirect":"signup"}


