from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}}, supports_credentials=True) # config les cross origin pour que toutes les origins soient ok ET que toutes les méthodes soient gérées autom  tiquement et qu'on doive pas le faire manuellement avec les requetes options par exmepl 

from db.package.user_management.user_creation import * # TRES important, on importe ici pour que le CORS soit appliqué à toutes les fonctions de user_creation, parce que la on lance le app.py donc on passe par le if __name__ ... mais quand on l'appelle d'autre part on lance pas le if __name__ == ... donc les azutres fonctions ont pas le parametrages de CORS 
from db.package.user_management.user_login import *
from db.package.institutions_management.send_all_institutions import *
from db.package.institutions_management.institution_login import *

# @app.route('/', methods=['OPTIONS', 'POST'])
# def test() : 
#     print ("Yo test réussi")
#     return '-- ok status --' 

#pas compris pourquoi je dois supprimer la fonction test ===> DEMANDER A GPTO

if __name__ == '__main__' : 
    app.run(host='0.0.0.0', port=5000, debug=True)