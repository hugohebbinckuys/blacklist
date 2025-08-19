- imports absolus pour pas de pb d'imports (p/ex from mon_projet.utils import ma_fonction)

- lancer avec python -m ...... .main par exemple 

- commande pour lancer serveur flask : (etre dans 'BLACKLIST') python -m db.package.app 


pourquoi pas faire 2 bdd distinctes : 1 pour user et 1 pour blacklist au vu du peu de ressource auquel on a le droit pour une bdd avec alwaysdata ? 



/!\ A faire plus tard : gérer les inscriptions en envoyant une requete de validation auprès du "responsable" de létablissement dans l'application pour pas que n'importe qui se connecte à la blackliste (=> ca signifie que on doit rajouter un status d'utilisateur pour avoir un SuperUser pour ce genre de choses)
