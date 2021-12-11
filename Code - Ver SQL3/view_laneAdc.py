import sqlite3

Requete = "SELECT Nom, Nom_lane FROM Champion, Lanes, Jouabilite WHERE Champion*id_ch = Jouabilite*id_ch AND Jouabilite*id_ch AND Jouabilite*No_lane = Lanes*No_lane AND Nom_lane = Adc"

conn = sqlite3.connect('League Project')

cur = conn.cursor()

cur.execute(Requete)

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
			<title>BD LOL Lane Adc</title>
		</head>
		<body>
			<h3>Lane Adc</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Nom du Champion</td>
					<td>Lane du Champion</td>
				</tr>
			</table>
			</form><BR>
				<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Nom_lane in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Nom_lane , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()