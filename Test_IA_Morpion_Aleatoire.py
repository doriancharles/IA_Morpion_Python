from random import randint

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
	
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "O" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "X") :
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
			victoire(premier_joueur,joueur,plateau)	
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)		
		else : 
			egalite(plateau)
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)	
	afficher(plateau)
	return plateau
	
def mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau_precedent[ligne][colonne] = "O"
	else :
		plateau_precedent[ligne][colonne] = "X"
	return plateau_precedent

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.	
def estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) :
	
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :								
		return False
									
def traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) != False :
		plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix)
	return plateau

#Traduit un choix en coordonnées (ligne et colonne) qu'il retourne dans une liste.
def traduction_choix(choix) :
	
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
	coordonnees = [ligne,colonne]
	return coordonnees
	
def traduction_coordonnees(ligne,colonne) :
	
	if ligne == 0 and colonne == 0 :
		choix = 1
	if ligne == 0 and colonne == 1 :
		choix = 2
	if ligne == 0 and colonne == 2 :
		choix = 3
	if ligne == 1 and colonne == 0 :
		choix = 4
	if ligne == 1 and colonne == 1 :
		choix = 5
	if ligne == 1 and colonne == 2 :
		choix = 6
	if ligne == 2 and colonne == 0 :
		choix = 7
	if ligne == 2 and colonne == 1 :
		choix = 8
	if ligne == 2 and colonne == 2 :
		choix = 9
	return choix

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau) :
				
	afficher(plateau)
	if joueur == "joueur" :	
		print("Vous avez gagné")				
	else :				
		print("L'IA a gagné")						

#Affiche qu'il y a égalité.			
def egalite(plateau) :
		
	afficher(plateau)
	print("Il y a égalité.")	

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

#Compte le nombre de cases complétées et retourne True si elles le sont toutes.			
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(0,len(plateau)) :
		for j in range(0,len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 9 :
		return True			

def decision(plateau,joueur,premier_joueur,symbole) :

	erreur = 1
	choix = randint(1,9)
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	while erreur == 1 :
		if estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) == False :
			choix = randint(1,9)
			coordonnees = traduction_choix(choix)
			ligne = coordonnees[0]
			colonne = coordonnees[1]
		else :
			break	
	return choix 

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.
def changer(joueur) :
	
	if joueur == "IA" :
		joueur = "joueur"
	else :
		joueur = "IA" 
	return joueur

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.
def enlever(choix,plateau) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix
	return plateau

def morpion() :
		
	print("Test IA morpion aleatoire")
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	premier_joueur = "joueur"
	joueur = "joueur"
	# Si vous voulez essayer la partie où le joueur a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 207 et 209
	# Enlevez les # des lignes 213 et 215
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer la partie où le joueur a choisi les X commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 213 et 215
	# Enlevez les # des lignes 207 et 209
	'''
	symbole = "X"
	'''	
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 219 et 295
	# Enlevez les # des lignes 299 et 378
	#'''
	if premier_joueur == "joueur" :
		for a in [1,2,3,4,5,6,7,8,9] :
			choix1 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
			joueur = changer(joueur)
			choix2 = decision(plateau,joueur,premier_joueur,symbole)
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
			joueur = changer(joueur)
			for b in [1,2,3,4,5,6,7,8,9] :
				choix3 = b
				plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3)
				if plateau != plateau_precedent :
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
					joueur = changer(joueur)
					choix4 = decision(plateau,joueur,premier_joueur,symbole)
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4)
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
					joueur = changer(joueur)
					for c in [1,2,3,4,5,6,7,8,9] :
						choix5 = c
						plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5)
						if plateau != plateau_precedent :
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
							joueur = changer(joueur)
							choix6 = decision(plateau,joueur,premier_joueur,symbole)
							plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6)
							if plateau != plateau_precedent :
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
								joueur = changer(joueur)
								for d in [1,2,3,4,5,6,7,8,9] :
									choix7 = d
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
										joueur = changer(joueur)
										choix8 = decision(plateau,joueur,premier_joueur,symbole)
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
											joueur = changer(joueur)
											for e in [1,2,3,4,5,6,7,8,9] :
												choix9 = e
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
											plateau = enlever(choix8,plateau)
											plateau_precedent = enlever(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = enlever(choix7,plateau_precedent)
										else :
											plateau = enlever(choix8,plateau)
											plateau_precedent = enlever(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = enlever(choix7,plateau_precedent)	
											joueur = changer(joueur)			
								plateau = enlever(choix6,plateau)
								plateau_precedent = enlever(choix6,plateau_precedent)
								plateau = enlever(choix5,plateau)
								plateau_precedent = enlever(choix5,plateau_precedent)
							else :	
								plateau = enlever(choix6,plateau)
								plateau_precedent = enlever(choix6,plateau_precedent)
								plateau = enlever(choix5,plateau)
								plateau_precedent = enlever(choix5,plateau_precedent)
								joueur = changer(joueur)
					plateau = enlever(choix4,plateau)
					plateau_precedent = enlever(choix4,plateau_precedent)
					plateau = enlever(choix3,plateau)
					plateau_precedent = enlever(choix3,plateau_precedent)
			plateau = enlever(choix2,plateau)
			plateau_precedent = enlever(choix2,plateau_precedent)
			plateau = enlever(choix1,plateau)
			plateau_precedent = enlever(choix1,plateau_precedent)	
	#'''			
	# Si vous voulez essayer la partie où l'IA commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostroples des lignes 298 et 377
	# Enlevez les # des lignes 215 et 294
	'''
	premier_joueur = "IA"
	joueur = "IA"
	if premier_joueur == "IA" :	
		choix1 = decision(plateau,joueur,premier_joueur,symbole)
		plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1)
		plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
		joueur = changer(joueur)
		for a in [1,2,3,4,5,6,7,8,9] :
			joueur = "joueur"
			choix2 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2)
			if plateau != plateau_precedent :
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
				joueur = changer(joueur)
				choix3 = decision(plateau,joueur,premier_joueur,symbole)
				plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3)
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
				joueur = changer(joueur)
				for b in [1,2,3,4,5,6,7,8,9] :
					joueur = "joueur"
					choix4 = b
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4)
					if plateau != plateau_precedent :
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
						joueur = changer(joueur)
						choix5 = decision(plateau,joueur,premier_joueur,symbole)
						plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5)
						if plateau != plateau_precedent :
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
							joueur = changer(joueur)
							for c in [1,2,3,4,5,6,7,8,9] :
								joueur = "joueur"
								choix6 = c
								plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6)
								if plateau != plateau_precedent :
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
									joueur = changer(joueur)
									choix7 = decision(plateau,joueur,premier_joueur,symbole)
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
										joueur = changer(joueur)
										for d in [1,2,3,4,5,6,7,8,9] :
											joueur = "joueur"
											choix8 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												joueur = changer(joueur)
												choix9 = decision(plateau,joueur,premier_joueur,symbole)
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9)
												plateau = enlever(choix8,plateau)
												plateau_precedent = enlever(choix8,plateau_precedent)	
												joueur = changer(joueur)			
										plateau = enlever(choix7,plateau)
										plateau_precedent = enlever(choix7,plateau_precedent)
										plateau = enlever(choix6,plateau)
										plateau_precedent = enlever(choix6,plateau_precedent)
									else :	
										plateau = enlever(choix7,plateau)
										plateau_precedent = enlever(choix7,plateau_precedent)
										plateau = enlever(choix6,plateau)
										plateau_precedent = enlever(choix6,plateau_precedent)	
										joueur = changer(joueur)				
							plateau = enlever(choix5,plateau)
							plateau_precedent = enlever(choix5,plateau_precedent)
							plateau = enlever(choix4,plateau)
							plateau_precedent = enlever(choix4,plateau_precedent)
						else :
							plateau = enlever(choix5,plateau)
							plateau_precedent = enlever(choix5,plateau_precedent)
							plateau = enlever(choix4,plateau)
							plateau_precedent = enlever(choix4,plateau_precedent)
							joueur = changer(joueur)
				plateau = enlever(choix3,plateau)
				plateau_precedent = enlever(choix3,plateau_precedent)
				plateau = enlever(choix2,plateau)
				plateau_precedent = enlever(choix2,plateau_precedent)
	'''
morpion()		
