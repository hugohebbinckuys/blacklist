from db.package.app import app
import flask
from flask import request
import bcrypt
from db.package._sql_requests.institution_requests import get_institution_by_id
from db.package._sql_requests.user_requests import put_institution_access_to_ok, get_user_information

@app.route("/institution_login", methods=["POST"])
def institution_login () : 
    sent = request.json
    email = sent.get("user_email")
    password_entered = sent.get("password_entered")
    institution_id = sent.get("institution_id")
    print (password_entered)
    print (institution_id)
    institution_password = get_institution_by_id(institution_id)
    print (institution_password)

    if (bcrypt.checkpw(password_entered.encode('utf-8'), institution_password[0].encode('utf-8'))) :
        # mettre à 1 le authorized sur la bdd 
        update_result = put_institution_access_to_ok(email)
        print (update_result)
        user = get_user_information(email)
        print("user : ", user)
        return {"status": "OK", "user_updated":user, "redirect":"connected/menu"}
    else : 
        return {"status":"KO", "redirect":"institution_auth"}
