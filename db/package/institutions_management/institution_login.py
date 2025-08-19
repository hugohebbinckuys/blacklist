from db.package.app import app

import flask
from flask import request

import bcrypt
from db.package.institutions_management.get_institution import get_institution_by_id

@app.route("/institution_login", methods=["POST"])
def institution_login () : 
    sent = request.json
    password_entered = sent.get("password_entered")
    institution_id = sent.get("institution_id")
    print (password_entered)
    print (institution_id)
    institution_password_tuple = get_institution_by_id(institution_id)
    institution_password = institution_password_tuple[0]
    print (institution_password)

    if (bcrypt.checkpw(institution_password.encode('utf-8'), password_entered.encode('utf-8'))) :
        return {"status": "OK", "redirect":"connected/menu", "comment" : "il faudra d'abord modifier la bdd et mettre 1 au lieu de zéro pour l'utilisateur"}
    else : 
        return {"status":"KO", "redirect":"institution_auth"}
