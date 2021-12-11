#!/usr/bin/env python3
import sqlite3

Requete = """SELECT Nom, Arme FROM Champions WHERE Arme="Faucille" OR Arme="Lampadaire";"""

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
			<title>BD LOL Armes Faucille Lampadaire</title>
		</head>
		<body>
			<h3>Armes Faucille Lampadaire</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Nom du Champion</td>
					<td>Arme du Champion</td>
				</tr>
			</table>
			</form><BR>
				<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Arme in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Arme , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()
