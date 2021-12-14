#!/usr/bin/env python3
import sqlite3
import random


conn = sqlite3.connect('League Project')
cur = conn.cursor()

#Table Partie

#Nb_drake = [0 ; 6]
drake = random.randint(0,6)

#Nb_herald = [0 ; 2]
herald = random.randint(0,2)

#Nb_nashor = [0 ; 2]
nashor = random.randint(0,2)

#Gagnant = [0 ; 2]
gagnant = random.randint(0,2)

#Tourelles = [0 ; 22]
tourelles = random.randint(0,22)

#Inhibiteur = [0 ; 6]
inhibiteur = random.randint(0,6)

#Ajout de valeurs dans la BD

Requete= "INSERT INTO Partie (Nb_drake, Nb_herald, Nb_nashor, Gagnant, Nb_tourelles, Inhibiteur) VALUES ("+str(drake)+","+str(herald)+","+str(nashor)+","+str(gagnant)+","+str(tourelles)+","+str(inhibiteur)+");"
cur.execute(Requete)
conn.commit()

print("Content-type: text/html")
print("\n\n")

#Table Resume Joueurs 

#suppression des anciennes valeurs
Requete = """DELETE FROM Resume_partie;"""

for i in range(10) :
    #Pseudo
    pseudo = random.randint(1,10)
    
    #Champion
    champion = random.randint(1,25)
    
    #skin 
    Req = "SELECT ID_skin FROM Skins WHERE ID_ch = "+str(champion)+";"
    cur.execute(Requete)
    skin = random.randint(0,1)
    
        
    #KDA = (0 , 20)(0 , 20)(0 , 20)
    tmp = (random.randint(0,20), random.randint(0,20), random.randint(0,20))
    KDA = str(str(tmp[0])+"/"+str(tmp[1])+"/"+str(tmp[2]))
    
    #Item
    item = random.randint(0,20)
    
    #Ajout des valeurs dans la BD
    Requete = "INSERT INTO Resume_partie (ID_joueur, ID_ch, ID_skin, KDA, ID_item) VALUES("+str(pseudo)+","+str(champion)+","+str(skin)+","+KDA+","+str(item)+")"
    cur.execute(Requete)
    conn.commit()

for i in range (5) :
    equipe = 1
    
    Requete = "INSERT INTO Resume_partie (Equipe) VALUES("+str(equipe)+")"
    cur.execute(Requete)
    conn.commit()
    
for i in range (5) :
    equipe = 2
    
    Requete = "INSERT INTO Resume_partie (Equipe) VALUES("+str(equipe)+");"
    cur.execute(Requete)
    conn.commit()
    

#affichage table 1
Requete = "SELECT Pseudo, Niveau, Rang, Victoires, Defaites, XP, LP FROM Joueurs;"
cur.execute(Requete)

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
			<title>BD LOL Simulation de partie</title>
		</head>
		<body>
			<h3>Joueurs</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Pseudo</td>
					<td>LVL</td>
					<td>Rank</td>
					<td>XP</td>
					<td>LP</td>
					<td>Nb parties gagnees</td>
					<td>Nb parties perdues</td>
				</tr>
			</table>
		</body>
	</html>""" )
    
for Pseudo, Niveau, Rang, Victoires, Defaites, XP, LP in cur.fetchall() :
    print(     """<tr>
                    <td>""", Pseudo , """</td>
                    <td>""", Niveau , """</td>
                    <td>""", Rang , """</td>
                    <td>""", Victoires , """</td>
                    <td>""", Defaites , """</td>
                    <td>""", XP , """</td>
                    <td>""", Defaites , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

#affichage table 2

Requete = "SELECT * FROM Partie;"
cur.execute(Requete)

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
		</head>
			<h3>Resume Partie</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Numero</td>
					<td>Nb drake</td>
					<td>Nb herald</td>
					<td>Nb nashor</td>
					<td>Equipe gagnante</td>
					<td>Tourelles</td>
					<td>Inhibiteur</td>
				</tr>
			</table>
		</body>
	</html>""" )
    
for ID_partie, Nb_drake, Nb_herald, Nb_nashor, Gagnant, Perdant, Nb_tourelles, Inhibiteur in cur.fetchall() :
    print(     """<tr>
                    <td>""", ID_partie , """</td>
                    <td>""", Nb_drake , """</td>
                    <td>""", Nb_herald , """</td>
                    <td>""", Nb_nashor , """</td>
                    <td>""", Gagnant , """</td>
                    <td>""", Perdant , """</td>
                    <td>""", Nb_tourelles , """</td>
                    <td>""", Inhibiteur , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

#affichage table 3

Requete = "SELECT Pseudo, ID_partie, Nom, Nom_skin, Equipe, KDA, Nom_item FROM Joueurs, Resume_partie, Champions, Skins, Boutique_Items WHERE Resume_partie.ID_ch = Champions.ID_ch AND Resume_partie.ID_joueur = Joueurs.ID_joueur AND Resume_partie.ID_skin = Skins.ID_skin AND Resume_partie.ID_item = Boutique_Items.ID_item;SELECT Pseudo, ID_partie, Nom, Nom_skin, Equipe, KDA, Nom_item FROM Joueurs, Resume_partie, Champions, Skins, Boutique_Items WHERE Resume_partie.ID_ch = Champions.ID_ch AND Resume_partie.ID_joueur = Joueurs.ID_joueur AND Resume_partie.ID_skin = Skins.ID_skin AND Resume_partie.ID_item = Boutique_Items.ID_item;"
cur.execute(Requete)

print( """<!doctype html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html;charset=iso-8859-2">
			<link rel="stylesheet" href="images/style.css" type="text/css" />
		</head>
		<body>
			<h3>Resume Joueurs</h3>
			<table border="1" cellpadding="5">
				<tr>
					<td>Pseudo</td>
					<td>Champion</td>
					<td>Skin</td>
					<td>Equipe</td>
					<td>KDA</td>
					<td>Item choisis</td>
				</tr>
			</table>
			</form><BR>
				<BR><form action="view_simulationPartie.py" method="">
					<input type="submit" value="Lancer une nouvelle partie" />
			</form><BR>
			</form>
				<form action="index.py" method="">
				<input type="submit" value="Accueil" />
			</form><BR>
		</body>
	</html>""" )
    
for Pseudo, Nom, Nom_skin, Equipe, KDA, Nom_item in cur.fetchall() :
    print(     """<tr>
                    <td>""", Pseudo , """</td>
                    <td>""", Nom , """</td>
                    <td>""", Nom_skin , """</td>
                    <td>""", Equipe , """</td>
                    <td>""", KDA , """</td>
                    <td>""", Nom_item , """</td>
                    </tr>""")
print( """</table>
        </body>
    </html>"""   )

conn.close()