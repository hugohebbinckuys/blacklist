from db.package.connexion import connexion
from db.package.app import app
import requests # bibliothèque python pr faire des requetes HTTP
from flask import request # objet fourin par flask pour récupérer les données de la reuqste http recue par le serveur flask (les headers, le contenu etc.)
from flask_cors import CORS, cross_origin

from db.package.utils import password_hacher

cursor = connexion.cursor 
db = connexion.db

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/', methods=['OPTIONS', 'POST'])
def test() : 
    print ("Yo test réussi")
    return '-- ok status --' 

@app.route("/new_user", methods=["POST"])
def new_user () : 
    sent = request.json 
    user = (sent.get("email"), password_hacher(sent.get("password")), sent.get("job"))
    try : 
        query = "INSERT INTO user VALUES(%s, %s, %s)"
        cursor.execute(query, user)

        db.commit()
        print ("\n--- values sent ---\n")

        return "-- ok status --"
    except Exception as e: 
        print ("\n--- Values didn't arrived to the db ---\n")
        print (e)

        return "-- KO status --"


