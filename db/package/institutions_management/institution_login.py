from db.package.app import app
import flask
from flask import request
import bcrypt
from db.package._sql_requests.institution_requests import get_institution_by_id

@app.route("/institution_login", methods=["POST"])
def institution_login () : 
    sent = request.json
    password_entered = sent.get("password_entered")
    institution_id = sent.get("institution_id")
    print (password_entered)
    print (institution_id)
    institution_password = get_institution_by_id(institution_id)
    print (institution_password)

    if (bcrypt.checkpw(password_entered.encode('utf-8'), institution_password[0].encode('utf-8'))) :
        return {"status": "OK", "redirect":"connected/menu", "comment" : "il faudra d'abord modifier la bdd et mettre 1 au lieu de zéro pour l'utilisateur"}
    else : 
        return {"status":"KO", "redirect":"institution_auth"}
