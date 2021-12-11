#!/usr/bin/env python3
import sqlite3

Requete = """Select "Nom",	"Sexe",
	"Arme",
	"Prix",
	"Date_ch",
	"Role",
	"A"	,
	"Z",
	"E"	,
	"R"	FROM Champions,Boutique_Items, Statistiques
	where 
	Boutique_Items.ID_item = Champions.ID_item
	AND Statistiques.ID_stat = Champions.ID_ch
	AND champions.Nom like "A%";"""


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
			<title>BD LOL Champion A</title>
		</head>
		<body>
			 <h3>Champion A</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Nom du Champion</td>
					<td>Prix</td>
					<td>Date</td>
					<td>Items conseilles</td>
					<td>A</td>
					<td>Z</td>
					<td>E</td>
					<td>R</td>
					<td>HP</td>
					<td>Mana</td>
					<td>AD</td>
					<td>AS</td>
					<td>AR</td>
					<td>MR</td>
					<td>Range</td>
				</tr>
			</table>
			</form><BR>
            	<BR><form action="index.py" method="">
					<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Nom, Prix_ch, Date_ch, Nom_item, A, Z, E, R, HP, Mana, AD, AS, AR, MR, Range in cur.fetchall() :
    print(     """<tr>
                    <td>""", Nom , """</td>
                    <td>""", Prix_ch , """</td>
                    <td>""", Date_ch , """</td>
                    <td>""", Nom_item , """</td>
                    <td>""", A , """</td>
                    <td>""", Z , """</td>
                    <td>""", E , """</td>
                    <td>""", R , """</td>
                    <td>""", HP , """</td>
                    <td>""", Mana , """</td>
                    <td>""", AD , """</td>
                    <td>""", AS , """</td>
                    <td>""", AR , """</td>
                    <td>""", MR , """</td>
                    <td>""", Range , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()
