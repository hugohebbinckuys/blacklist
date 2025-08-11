import bcrypt

def password_hacher (passwd) : 
    salt = bcrypt.gensalt(12)
    hash_password = bcrypt.hashpw(passwd.encode('utf-8'), salt)
    return hash_password