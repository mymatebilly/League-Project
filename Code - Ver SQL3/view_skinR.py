import sqlite3

Requete = "SELECT Nom, Nom_skin, Prix_skin, Date_skin FROM Champion, Skins, Alphabet WHERE Champion*id_ch = Skins*id_ch AND Champion*id_ch = Alphabet*id_ch AND Lettre = R"

conn = sqlite3.connect('League Project')

cur = conn.cursor()

cur.execute(Requete)

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
			<title>BD LOL Skin R</title>
		</head>
		<body>
			<h3>Skin R</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Nom du Champion</td>
					<td>Nom du Skin</td>
					<td>Prix</td>
					<td>Date</td>
				</tr>
			</table>
			</form><BR>
				<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Nom_skin, Prix_skin, Date_skin in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Nom_skin , """</td>
                    <td>""", Prix_skin , """</td>
                    <td>""", Date_skin , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()