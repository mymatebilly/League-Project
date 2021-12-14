#!/usr/bin/env python3
import sqlite3

Requete = """SELECT Nom, Sexe FROM Champions WHERE Sexe = "F";"""

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
			<title>BD LOL Genre F</title>
		</head>
		<body>
			<h3>Genre F</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Nom Champion</td>
					<td>Genre Champion</td>
				</tr>
			</table>
			</form><BR>
				<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Sexe in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Sexe , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()