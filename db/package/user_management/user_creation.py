import connexion

cursor = connexion.cursor 
db = connexion.db

test_email = "hugo29.heb@gmail.com"
password = "test"
job = "receptionniste"

parameters = (test_email, password, job)
try : 
    query = "INSERT INTO user VALUES(%s, %s, %s)"
    cursor.execute(query, parameters)

    db.commit()
    print ("\n--- values sent ---\n")
except : 
    print ("\n--- Values didn't arrived to the db ---\n")

cursor.close()