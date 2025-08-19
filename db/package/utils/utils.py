import bcrypt

from db.package.utils.db_requests.get_requests import get_all_instutions, get_all_user_email_passwd_authorized

from db.package.connexion.connexion import db
from db.package.connexion.connexion import cursor


def password_hacher (passwd) : 
    salt = bcrypt.gensalt(12)
    hash_password = bcrypt.hashpw(passwd.encode('utf-8'), salt)
    return hash_password

def get_all_institutions_request () : 
    request = get_all_instutions
    cursor.execute(request)
    response = cursor.fetchall()
    return response

def get_user_information (email) :
    request = get_all_user_email_passwd_authorized(email)
    cursor.execute(request)
    response = cursor.fetchall()
    return response