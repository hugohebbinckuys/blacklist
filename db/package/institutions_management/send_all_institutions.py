from db.package.app import app
from db.package.utils.utils import get_institutions_request

@app.route("/recup_institutions", methods=["GET"])
def send_institutions_to_vuejs () :
    institutions = get_institutions_request()
    return {"institutions" : institutions, "format de reponse :" : "[(id, 'name', 'location', 'password')]"}