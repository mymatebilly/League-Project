#!/usr/bin/python
import psycopg2
import cgi

hostname = 'localhost'
username = 'postgres'
password = 'C1c0mbl3!'
database = 'postgres'

requete = """INSERT INTO client (id_client,nom,prenom,adresseclient,villeclient,cpclient)  VALUES('%s','%s','%s','%s','%s','%s')"""
requetemaxID = """select id_client+1 from client order by id_client desc limit 1"""

Page = """
<!doctype html>
	<html lang="fr">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
            <link rel="stylesheet" href="images/style.css" type="text/css" />
			<title>Gestion du Camping</title>
		</head>
		<body>
             <form action="view_resa_tente.py" method="post">
					<input type="submit" value="Reserver pour une Tente" name="id_client" />
			</form><BR>
            <form action="view_resa_mobilhome.py" method="post">
					<input type="submit" value="Reserver un Mobil-Home" name="id_client" />
			</form><BR>
            <form action="view_resa_caravane.py" method="post">
					<input type="submit" value="Reserver une Caravane" name="id_client" />
			</form><BR>
            <BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>"""

 
# Recuperation des variables du fichier views.py
form = cgi.FieldStorage()

# Variables locales qui permettent de recuperer les valeurs du formulaire
conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

curMax = conn.cursor()
curMax.execute(requetemaxID)
maxId = curMax.fetchone()

id_client = requetemaxID[0]
nom = form["nom"].value
prenom = form["prenom"].value
adresse = form["adresse"].value
ville = form["ville"].value
cp = form["cp"].value

cur = conn.cursor()
cur.execute( requete % (id_client,nom,prenom,adresse,ville,cp))
conn.commit()
conn.close()

print(Page)


