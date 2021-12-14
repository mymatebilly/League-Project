#!/usr/bin/env python3
import sqlite3

Requete = """Select Nom,
	Nom_skin,
	Prix_skin,
	Date_skin
	FROM Champions, Skins 
	where 
	Skins.ID_ch = Champions.ID_ch
	AND Champions.Nom like "A%";"""

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
			<title>BD LOL Skin A</title>
		</head>
		<body>
			<h3>Skin A</h3>
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