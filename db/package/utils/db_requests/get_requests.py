def get_all_user_email_passwd_authorized (email) :
    return f"SELECT * FROM user where user.email = '{email}'"

get_all_instutions = "SELECT * from institution"

def get_institution_by_id_request (id) : 
    return f"SELECT password from institution where institution.id = '{id}'"