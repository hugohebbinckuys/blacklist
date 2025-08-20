from db.package.connexion.connexion import db, cursor
from db.package.app import app
import requests # bibliothèque python pr faire des requetes HTTP
from flask import request # objet fourin par flask pour récupérer les données de la reuqste http recue par le serveur flask (les headers, le contenu etc.)
from db.package.utils.utils import password_hacher
from db.package._sql_requests.user_requests import insert_new_user, get_user_information


@app.route("/new_user", methods=["POST"])
def new_user () : 
    sent = request.json 
    user = (sent.get("email"), password_hacher(sent.get("password")), sent.get("job"), sent.get("institution"))
    try : 
        insert_new_user(user)
        
        authorized_request = get_user_information(user[0])
        print ("\n athorized_request : ", authorized_request)
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


