from db.package.connexion import connexion
from db.package.app import app
import flask
from flask import request
from flask_bcrypt import bcrypt

from db.package.db_requests.get_requests import get_user_email_passwd


db = connexion.db
cursor = connexion.cursor

@app.route("/login", methods=["POST"])
def login () : 
    sent = request.json
    email = sent.get("email")
    password = sent.get("password")
    print ("credentials reçues : ", email, password)


    cursor.execute(get_user_email_passwd)
    all_users = cursor.fetchall() # renvoie bien une liste de tuple qui contient les infos de l'user (ici email, password)

    for user in all_users : 
        print ("\n-user : ", user, " -")
        if user[0] == email : 
            if (bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8'))) :
                return {'authorized' : True}
            else : return {'authorized': False, 'password': 'NOT ok'}
    print ("user '"+email+"' inexistant")
    return {'authorized': False, 'user': 'NOT exists'}


