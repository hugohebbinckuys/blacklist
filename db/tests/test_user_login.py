from db.package.connexion import connexion
from db.package.app import app
import flask
from flask import request
from flask_bcrypt import bcrypt
from db.package.utils.db_requests.get_requests import get_user_email_passwd


db = connexion.db
cursor = connexion.cursor

def login () : 
    # email = "hugo"
    # clear_password = "test"
    email = "hugo29.heb@gmail.com"
    clear_password = "hugo"

    cursor.execute(get_user_email_passwd)
    all_users = cursor.fetchall() # renvoie bien une liste de tuple qui contient les infos de l'user (ici email, password)

    for user in all_users : 
        print ("\n-user : ", user, " -")
        if user[0] == email : 
            return bcrypt.checkpw(clear_password.encode('utf-8'), user[1].encode('utf-8'))
    print ("user '"+email+"' inexistant")
    return False


if __name__ == "__main__" : 
    print (login())