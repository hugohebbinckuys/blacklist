import mysql, mysql.connector

try :
    db = mysql.connector.connect(
        host="mysql-blacklist-db.alwaysdata.net", 
        user="425889_hh",
        password=".jkEqv@wQe2976U",
        database="blacklist-db_01"
    )

    cursor = db.cursor()
    print ("\n--- connected to the db ---\n")

except : 
    print("\n--- error when trying to connect to the database ---\n")

