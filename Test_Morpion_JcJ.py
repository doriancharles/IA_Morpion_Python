#Affiche les 3 valeurs de chaque lignes, dans l'ordre, lignes par lignes.
def afficher(plateau) :
	
	for i in range(0,len(plateau)) :		
		print(plateau[i])	
	#Faites les instructions suivantes sur les lignes 9 et 11, si ce n'est pas déjà fait :
	#- Mettez des # devant les 3 apostrophes si vous voulez sauter une ligne après les résultats 
	#- Enlevez les # si vous ne voulez pas 
	#Sauter une ligne peut empêcher de voir tous les résultats
	'''
	print ("")
	'''

#Vérifie que le joueur actuel a les ronds et retourne True si c'est le cas.	
def aLesRonds(joueur,premier_joueur,symbole) :
	
	if (joueur == "joueur 1" and premier_joueur == "joueur 1" and symbole == "O" or
	joueur == "joueur 1" and premier_joueur == "joueur 2" and symbole == "O" or
	joueur == "joueur 2" and premier_joueur == "joueur 1" and symbole == "X" or
	joueur == "joueur 2" and premier_joueur == "joueur 2" and symbole == "X") :			
		return True
	
#Met le symbole du joueur actuel à une place correspondante à un choix valide puis vérifie si il a gagné ou si il y a égalité.	
def placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"		
	else :		
		plateau[ligne][colonne] = "X"	
	if estVictorieux(plateau) == True :
		victoire(joueur,plateau)
		plateau = enlever(choix,plateau)
		plateau_precedent = enlever(choix,plateau_precedent)
	if estEgalitaire(plateau) == True :
		if estVictorieux(plateau) == True :
			joueur = changer(joueur)
			victoire(joueur,plateau)
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)
		else : 
			egalite(plateau)
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)
	return plateau

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.						
def estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		if plateau[ligne][colonne] == "O" :
			return False
		if plateau[ligne][colonne] == "X" :
			return False
	else :
		if plateau[ligne][colonne] == "X" :
			return False	 
		if plateau[ligne][colonne] == "O" :							
			return False

#Traduit un choix en coordonnées (ligne et colonne) qu'il retourne dans une liste.		
def traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix) :	
	
	if choix == 1 or choix == 2 or choix == 3 :
		ligne = 0
	if choix == 4 or choix == 5 or choix == 6 :
		ligne = 1
	if choix == 7 or choix == 8 or choix == 9 :
		ligne = 2
	if choix == 1 or choix == 4 or choix == 7 :
		colonne = 0
	if choix == 2 or choix == 5 or choix == 8 :
		colonne = 1 
	if choix == 3 or choix == 6 or choix == 9 :
		colonne = 2
	if estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) != False :
		plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix) 
	return plateau

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau) :
	
	print("Le " , joueur , " a gagné")
	print("")
	afficher(plateau)

#Affiche qu'il y a égalité.	
def egalite(plateau) :
	
	print("Il y a égalité.")
	print("")
	afficher(plateau)

#Vérifie si il y a un gagnant et retourne True si c'est le cas.	
def estVictorieux(plateau) :
	
	if plateau[0][0] == "X" and plateau[0][1] == "X" and plateau[0][2] == "X" : 
		return True
	if plateau[1][0] == "X" and plateau[1][1] == "X" and plateau[1][2] == "X" :
		return True
	if plateau[2][0] == "X" and plateau[2][1] == "X" and plateau[2][2] == "X" :
		return True
	if plateau[0][0] == "X" and plateau[1][0] == "X" and plateau[2][0] == "X" :
		return True
	if plateau[0][1] == "X" and plateau[1][1] == "X" and plateau[2][1] == "X" :
		return True
	if plateau[0][2] == "X" and plateau[1][2] == "X" and plateau[2][2] == "X" :
		return True
	if plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == "X" :
		return True
	if plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == "X" :
		return True
	if plateau[0][0] == "O" and plateau[0][1] == "O" and plateau[0][2] == "O" : 
		return True
	if plateau[1][0] == "O" and plateau[1][1] == "O" and plateau[1][2] == "O" :
		return True
	if plateau[2][0] == "O" and plateau[2][1] == "O" and plateau[2][2] == "O" :
		return True
	if plateau[0][0] == "O" and plateau[1][0] == "O" and plateau[2][0] == "O" :
		return True
	if plateau[0][1] == "O" and plateau[1][1] == "O" and plateau[2][1] == "O" :
		return True
	if plateau[0][2] == "O" and plateau[1][2] == "O" and plateau[2][2] == "O" :
		return True
	if plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == "O" :
		return True
	if plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == "O" :
		return True

#Vérifie si il y a 8 cases complétées et retourne True si elles le sont toutes.
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(0,len(plateau)) :
		for j in range(0,len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 9 :
		return True		

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.
def changer(joueur) :
	
	if joueur == "joueur 1" :
		joueur = "joueur 2"
	else :
		joueur = "joueur 1" 
	return joueur
	
def annoncer_tour(joueur) :
	
	print("Au tour du",joueur)
	print("")

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.
def enlever(choix,plateau) :
	
	if choix == 1 or choix == 2 or choix == 3 :
		ligne = 0
	if choix == 4 or choix == 5 or choix == 6 :
		ligne = 1
	if choix == 7 or choix == 8 or choix == 9 :
		ligne = 2
	if choix == 1  or choix == 4 or choix == 7 :
		colonne = 0
	if choix == 2 or choix == 5 or choix == 8 :
		colonne = 1 
	if choix == 3 or choix == 6 or choix == 9 :
		colonne = 2
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix
	return plateau

def morpion() :
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	# Si vous voulez essayer pour quand le joueur 1 commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 163 et 166 
	# Enlevez les # des lignes 170 et 173
	#'''
	premier_joueur = "joueur 1"
	joueur = "joueur 1"
	#'''
	# Si vous voulez essayer pour quand le joueur 2 commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 170 et 173
	# Enlevez les # des lignes 163 et 166
	'''
	premier_joueur = "joueur 2"
	joueur = "joueur 2"
	'''
	# Si vous voulez essayer pour quand le joueur 1 a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 177 et 179
	# Enlevez les # des lignes 183 et 185
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer pour quand le joueur 1 a choisi les X et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 183 et 185
	# Enlevez les # des lignes 177 et 179
	'''
	symbole = "X"
	'''
	print("Test Morpion JcJ")
	print("")
	for a in [1,2,3,4,5,6,7,8,9] :
		choix1 = a
		plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1)
		plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix1)
		joueur = changer(joueur)
		for b in [1,2,3,4,5,6,7,8,9] :
			choix2 = b
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2)
			if plateau != plateau_precedent :
				plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix2)
				joueur = changer(joueur)
				for c in [1,2,3,4,5,6,7,8,9] :
					choix3 = c
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3)
					if plateau != plateau_precedent :
						plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix3)
						joueur = changer(joueur)
						for d in [1,2,3,4,5,6,7,8,9] :
							choix4 = d
							plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4)
							if plateau != plateau_precedent :
								plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix4)
								joueur = changer(joueur)
								for e in [1,2,3,4,5,6,7,8,9] :
									choix5 = e
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5)
									if plateau != plateau_precedent :
										plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix5)
										joueur = changer(joueur)
										for f in [1,2,3,4,5,6,7,8,9] :
											choix6 = f
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6)
											if plateau != plateau_precedent :
												plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix6)
												joueur = changer(joueur)
												for g in [1,2,3,4,5,6,7,8,9] :
													choix7 = g
													plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7)
													if plateau != plateau_precedent :
														plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix7)
														joueur = changer(joueur)
														for h in [1,2,3,4,5,6,7,8,9] :
															choix8 = h
															plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8)
															if plateau != plateau_precedent :
																plateau_precedent = traduction(joueur,premier_joueur,symbole,plateau_precedent,plateau_precedent,choix8)
																joueur = changer(joueur)
																for i in [1,2,3,4,5,6,7,8,9] :
																	choix9 = i
																	plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9)
																plateau = enlever(choix8,plateau)
																plateau_precedent = enlever(choix8,plateau_precedent)
																joueur = changer(joueur)
														plateau = enlever(choix7,plateau)
														plateau_precedent = enlever(choix7,plateau_precedent)
														joueur = changer(joueur)
												plateau = enlever(choix6,plateau)
												plateau_precedent = enlever(choix6,plateau_precedent)
												joueur = changer(joueur)
										plateau = enlever(choix5,plateau)
										plateau_precedent = enlever(choix5,plateau_precedent)
										joueur = changer(joueur)
								plateau = enlever(choix4,plateau)
								plateau_precedent = enlever(choix4,plateau_precedent)
								joueur = changer(joueur)
						plateau = enlever(choix3,plateau)
						plateau_precedent = enlever(choix3,plateau_precedent)
						joueur = changer(joueur)	
				plateau = enlever(choix2,plateau)
				plateau_precedent = enlever(choix2,plateau_precedent)
				joueur = changer(joueur)
		plateau = enlever(choix1,plateau)
		plateau_precedent = enlever(choix1,plateau_precedent)
		joueur = changer(joueur)							
																
morpion()
