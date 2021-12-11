#!/usr/bin/env python3
import sqlite3
import cgi

Requete = """SELECT Nom, Nom_lane FROM Champions, Lane, Jouabilite WHERE Champions.id_ch = Jouabilite.id_ch AND Jouabilite.id_ch AND Jouabilite.No_lane = Lane.No_Lane AND Nom_Lane = "Top";"""

conn = sqlite3.connect('League Project')

cur = conn.cursor()

cur.execute(Requete)

print("Content-type: text/html")
print("\n\n")

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
			<title>BD LOL Lane Top</title>
		</head>
		<body>
			<h3>Lane Top</h3>
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