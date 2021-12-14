#!/usr/bin/env python3
import sqlite3

Requete = """SELECT Nom, Role FROM Champions WHERE Role="Assassin";"""

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
			<title>BD LOL Role Assassin</title>
		</head>
		<body>
			<h3>Rôle Assassin</h3>
            <table border="1" cellpadding="5">
                <tr>
                    <td>Nom du Champion</td>
                    <td>Role du Champion</td>
                </tr>
			</table>
			</form><BR>
				<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Role in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Role , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()