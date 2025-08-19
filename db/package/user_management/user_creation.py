from db.package.connexion import connexion
from db.package.app import app

import requests # bibliothèque python pr faire des requetes HTTP

from flask import request # objet fourin par flask pour récupérer les données de la reuqste http recue par le serveur flask (les headers, le contenu etc.)
from flask_cors import CORS, cross_origin

from db.package.utils.utils import password_hacher

from db.package.utils.utils import get_user_information

cursor = connexion.cursor 
db = connexion.db

# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/', methods=['OPTIONS', 'POST'])
def test() : 
    print ("Yo test réussi")
    return '-- ok status --' 

@app.route("/new_user", methods=["POST"])
def new_user () : 
    sent = request.json 
    user = (sent.get("email"), password_hacher(sent.get("password")), sent.get("job"), sent.get("institution"))
    try : 
        query = "INSERT INTO user (email, password, job, institution_id) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, user)

        db.commit()
        print ("\n--- values sent ---\n")

        authorized_request = get_user_information(user[0])
        authorized = authorized_request[0][2]
        
        if (authorized == 1) :
            return {"status":"OK", "redirect":"connected", "user_info":authorized_request[0]}
        else : 
            return {"status":"OK", "redirect":"institution_auth", "user_info":authorized_request[0]}

    except Exception as e: 
        print ("\n--- Values didn't arrived to the db ---\n")
        print (e)

        return {"status":"KO", "redirect":"signup"}


