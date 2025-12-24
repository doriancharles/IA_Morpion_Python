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
		
def choix_miroir(choix) :
	
	choix_effectue = 0
	while choix_effectue == 0 :
		if choix == 1 :
			choix = 9
			break
		if choix == 2 :
			choix = 8
			break
		if choix == 3 :
			choix = 7
			break
		if choix == 4 :
			choix = 6
			break
		if choix == 6 :
			choix = 4
			break
		if choix == 7 :
			choix = 3
			break
		if choix == 8 :
			choix = 2
			break
		if choix == 9 :
			choix = 1
			break
	return choix

#Met le symbole du joueur actuel à une place correspondante à un choix valide puis vérifie si il a gagné ou si il y a égalité.		
def placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,tour) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"
	else :
		plateau[ligne][colonne] = "X"
	if estVictorieux(plateau) == True :		
		victoire(joueur,plateau)	
		plateau = enlever(choix,plateau)
		plateau_precedent = retirer(choix,plateau_precedent)
	if estEgalitaire(plateau) == True :		
		if estVictorieux(plateau) == True :			
			joueur = changer(joueur)
			victoire(joueur,plateau)	
			plateau = enlever(choix,plateau)
			plateau_precedent = retirer(choix,plateau_precedent)		
		else : 
			egalite(plateau)
			plateau = enlever(choix,plateau)
			plateau_precedent = retirer(choix,plateau_precedent)	
	afficher(plateau)
	return plateau

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.	
def estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) :
		
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		return False
	if joueur == "IA" :
		if empecheVictoire(premier_joueur,symbole,choix,plateau) == True :
			return False

#Traduit un choix en coordonnées (ligne et colonne) qu'il retourne dans une liste.
def traduction_choix(choix) :
		
	ligne = 0
	colonne = 0
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

def traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix,tour) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if joueur == "joueur" :
		if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) != False :
			coordonnees = traduction_choix(choix)
			ligne = coordonnees[0]
			colonne = coordonnees[1]
			plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,tour)
	if joueur == "IA" :
		plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,tour)
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

#Affiche le gagnant en l'informant de sa victoire.	
def victoire(joueur,plateau) :
	
	afficher(plateau)
	if joueur == "joueur" :
		print("Vous avez gagné")
	if joueur == "IA" :
		print("L'IA a gagné")

#Affiche qu'il y a égalité.			
def egalite(plateau) :
	
	afficher(plateau)
	print("Il y a égalité.")
	
def empecheVictoire(premier_joueur,symbole,choix,plateau) :
	
	if symbole == "X" :
		if choix == 1 :
			if (plateau[0][0] == 1 and plateau[0][1] == "O" and plateau[0][2] == "O" or	
			plateau[0][0] == 1 and plateau[1][0] == "O" and plateau[2][0] == "O" or
			plateau[0][0] == 1 and plateau[1][1] == "O" and plateau[2][2] == "O") :
				return True
		if choix == 2 :
			if (plateau[0][0] == "O" and plateau[0][1] == 2 and plateau[0][2] == "O" or
			plateau[0][1] == 2 and plateau[1][1] == "O" and plateau[2][1] == "O") :
				return True
		if choix == 3 :
			if (plateau[0][0] == "O" and plateau[0][1] == "O" and plateau[0][2] == 3 or
			plateau[0][2] == 3 and plateau[1][2] == "O" and plateau[2][2] == "O" or	
			plateau[0][2] == 3 and plateau[1][1] == "O" and plateau[2][0] == "O") :
				return True
		if choix == 4 :
			if (plateau[1][0] == 4 and plateau[1][1] == "O" and plateau[1][2] == "O" or
			plateau[0][0] == "O" and plateau[1][0] == 4 and plateau[2][0] == "O") :
				return True
		if choix == 5 :
			if (plateau[1][0] == "O" and plateau[1][1] == 5 and plateau[1][2] == "O" or
			plateau[0][1] == "O" and plateau[1][1] == 5 and plateau[2][1] == "O" or
			plateau[0][0] == "O" and plateau[1][1] == 5 and plateau[2][2] == "O" or
			plateau[0][2] == "O" and plateau[1][1] == 5 and plateau[2][0] == "O") :
				return True
		if choix == 6 :
			if (plateau[1][0] == "O" and plateau[1][1] == "O" and plateau[1][2] == 6 or
			plateau[0][2] == "O" and plateau[1][2] == 6 and plateau[2][2] == "O") :
				return True
		if choix == 7 :
			if (plateau[2][0] == 7 and plateau[2][1] == "O" and plateau[2][2] == "O" or
			plateau[0][0] == "O" and plateau[1][0] == "O" and plateau[2][0] == 7 or
			plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == 7) :
				return True
		if choix == 8 :
			if (plateau[2][0] == "O" and plateau[2][1] == 8 and plateau[2][2] == "O" or
			plateau[0][1] == "O" and plateau[1][1] == "O" and plateau[2][1] == 8) :
				return True
		if choix == 9 :
			if (plateau[2][0] == "O" and plateau[2][1] == "O" and plateau[2][2] == 9 or	
			plateau[0][2] == "O" and plateau[1][2] == "O" and plateau[2][2] == 9 or	
			plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == 9) :
				return True			
	if symbole == "O" :
		if choix == 1 :
			if (plateau[0][0] == 1 and plateau[0][1] == "X" and plateau[0][2] == "X" or
			plateau[0][0] == 1 and plateau[1][0] == "X" and plateau[2][0] == "X" or
			plateau[0][0] == 1 and plateau[1][1] == "X" and plateau[2][2] == "X") :
				return True
		if choix == 2 :
			if (plateau[0][0] == "X" and plateau[0][1] == 2 and plateau[0][2] == "X" or 
			plateau[0][1] == 2 and plateau[1][1] == "X" and plateau[2][1] == "X") :
				return True
		if choix == 3 :
			if (plateau[0][0] == "X" and plateau[0][1] == "X" and plateau[0][2] == 3 or
			plateau[0][2] == 3 and plateau[1][2] == "X" and plateau[2][2] == "X" or
			plateau[0][2] == 3 and plateau[1][1] == "X" and plateau[2][0] == "X") :
				return True
		if choix == 4 :
			if (plateau[1][0] == 4 and plateau[1][1] == "X" and plateau[1][2] == "X" or
			plateau[0][0] == "X" and plateau[1][0] == 4 and plateau[2][0] == "X") :
				return True
		if choix == 5 :
			if (plateau[1][0] == "X" and plateau[1][1] == 5 and plateau[1][2] == "X" or	
			plateau[0][1] == "X" and plateau[1][1] == 5 and plateau[2][1] == "X" or
			plateau[0][0] == "X" and plateau[1][1] == 5 and plateau[2][2] == "X" or
			plateau[0][2] == "X" and plateau[1][1] == 5 and plateau[2][0] == "X") :
				return True
		if choix == 6 :
			if (plateau[1][0] == "X" and plateau[1][1] == "X" and plateau[1][2] == 6 or
			plateau[0][2] == "X" and plateau[1][2] == 6 and plateau[2][2] == "X") :
				return True
		if choix == 7 :
			if (plateau[2][0] == 7 and plateau[2][1] == "X" and plateau[2][2] == "X" or
			plateau[0][0] == "X" and plateau[1][0] == "X" and plateau[2][0] == 7 or
			plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == 7) :
				return True
		if choix == 8 :
			if (plateau[2][0] == "X" and plateau[2][1] == 8 and plateau[2][2] == "X" or
			plateau[0][1] == "X" and plateau[1][1] == "X" and plateau[2][1] == 8) :
				return True
		if choix == 9 :
			if (plateau[2][0] == "X" and plateau[2][1] == "X" and plateau[2][2] == 9 or
			plateau[0][2] == "X" and plateau[1][2] == "X" and plateau[2][2] == 9 or
			plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == 9) :
				return True	

#Vérifie si il y a un gagnant et retourne True si c'est le cas.			
def estVictorieux(plateau) :
		
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

#Compte le nombre de cases complétées et retourne True si elles le sont toutes.				
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(len(plateau)) :
		for j in range(len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 9 :
		return True			

def decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour) :
						
	erreur = 1
	choix = randint(1,9)
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	while erreur == 1 :
		if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
			choix = randint(1,9)
			coordonnees = traduction_choix(choix)
			ligne = coordonnees[0]
			colonne = coordonnees[1]
		else :
			break				
	return choix

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.
def enlever(choix,plateau) :
		
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix
	return plateau

def retirer(choix,plateau_precedent) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau_precedent[ligne][colonne] == "O" or plateau_precedent[ligne][colonne] == "X" :
		plateau_precedent[ligne][colonne] = choix
	return plateau_precedent

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.	
def changer(joueur) :
	
	if joueur == "IA" :
		joueur = "joueur"
	else :
		joueur = "IA" 
	return joueur

def morpion() :
	
	print("Test IA morpion imperdable")
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	premier_joueur = "joueur"
	joueur = "joueur"
	ligne = 0
	colonne = 0
	tour = 0
	# Si vous voulez essayer la partie où le joueur 1 a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 341 et 343
	# Enlevez les # des lignes 347 et 349
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer la partie où le joueur 1 a choisi les X et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 347 et 349
	# Enlevez les # des lignes 341 et 343
	'''
	symbole = "X"
	'''	
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 353 et 714
	# Enlevez les # des lignes 544 et 623
	#'''			
	if premier_joueur == "joueur" :
		for a in [1,2,3,4,5,6,7,8,9] :
			choix1 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1,tour)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
			joueur = changer(joueur)
			if choix1 == 2 :
				choix2 = 8
				plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix2,tour)
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
				joueur = changer(joueur)
				for b in [1,2,3,4,5,6,7,8,9] :
					choix3 = b
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3,tour)
					if plateau != plateau_precedent :
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
						joueur = changer(joueur)
						if choix3 == 4 :
							choix4 = 6
							plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
							joueur = changer(joueur)
							for c in [1,2,3,4,5,6,7,8,9] :
								choix5 = c
								plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
								if plateau != plateau_precedent :
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
									joueur = changer(joueur)
									if choix5 == 1 :
										choix6 = 5
									else :
										choix6 = 1
									plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)	
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
									joueur = changer(joueur)
									for d in [1,2,3,4,5,6,7,8,9] :
										choix7 = d
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
											joueur = changer(joueur)	
											choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
											plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
											joueur = changer(joueur)
											for e in [1,2,3,4,5,6,7,8,9] :
												choix9 = e
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
											plateau = enlever(choix8,plateau)
											plateau_precedent = retirer(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = retirer(choix7,plateau_precedent)			
									plateau = enlever(choix6,plateau)
									plateau_precedent = retirer(choix6,plateau_precedent)
									plateau = enlever(choix5,plateau)
									plateau_precedent = retirer(choix5,plateau_precedent)								
						else :
							choix4 = 4
							placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
							joueur = changer(joueur)
							for c in [1,2,3,4,5,6,7,8,9] :
								choix5 = c
								plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
								if plateau != plateau_precedent :
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
									joueur = changer(joueur)
									if choix5 == 3 :
										choix6 = 5
										if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
											choix6 = 6
										plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
										joueur = changer(joueur)
									else :
										choix6 = 3
										if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
											choix6 = 5
											if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
												choix6 = 6
									plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
									joueur = changer(joueur)	
									for d in [1,2,3,4,5,6,7,8,9] :
										choix7 = d
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
											joueur = changer(joueur)	
											choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
											plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
											joueur = changer(joueur)
											for e in [1,2,3,4,5,6,7,8,9] :
												choix9 = e
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
											plateau = enlever(choix8,plateau)
											plateau_precedent = retirer(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = retirer(choix7,plateau_precedent)			
									plateau = enlever(choix6,plateau)
									plateau_precedent = retirer(choix6,plateau_precedent)
									plateau = enlever(choix5,plateau)
									plateau_precedent = retirer(choix5,plateau_precedent)					
			else : 
				choix2 = 2
				plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix2,tour)
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
				joueur = changer(joueur)
				for b in [1,2,3,4,5,6,7,8,9] :
					choix3 = b
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3,tour)
					if plateau != plateau_precedent :
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
						joueur = changer(joueur)
						if choix3 == 4 :
							choix4 = 6
							if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix4,tour) == False :
								choix4 = 7
								plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
								joueur = changer(joueur)
								for c in [1,2,3,4,5,6,7,8,9] :
									choix5 = c
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
										joueur = changer(joueur)
										if choix5 == 1 :
											choix6 = 3
										else :
											choix6 = 1
										plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
										joueur = changer(joueur)
										for d in [1,2,3,4,5,6,7,8,9] :
											choix7 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
												joueur = changer(joueur)	
												choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
												afficher(plateau)
												plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												joueur = changer(joueur)
												for e in [1,2,3,4,5,6,7,8,9] :
													choix9 = e
													plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
													if plateau != plateau_precedent :
														plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
												plateau = enlever(choix8,plateau)
												plateau_precedent = retirer(choix8,plateau_precedent)
												plateau = enlever(choix7,plateau)
												plateau_precedent = retirer(choix7,plateau_precedent)			
										plateau = enlever(choix6,plateau)
										plateau_precedent = retirer(choix6,plateau_precedent)
										plateau = enlever(choix5,plateau)
										plateau_precedent = retirer(choix5,plateau_precedent)
							else :
								plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
								joueur = changer(joueur)
								for c in [1,2,3,4,5,6,7,8,9] :
									choix5 = c
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
										joueur = changer(joueur)
										if choix5 == 7 :
											choix6 = 5
											if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
												choix6 = 8
										else :
											choix6 = 7
											if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
												choix6 = 5
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 8
										plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
										joueur = changer(joueur)	
										for d in [1,2,3,4,5,6,7,8,9] :
											choix7 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
												joueur = changer(joueur)	
												choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
												plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												joueur = changer(joueur)
												for e in [1,2,3,4,5,6,7,8,9] :
													choix9 = e
													plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
													if plateau != plateau_precedent :
														plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
												plateau = enlever(choix8,plateau)
												plateau_precedent = retirer(choix8,plateau_precedent)
												plateau = enlever(choix7,plateau)
												plateau_precedent = retirer(choix7,plateau_precedent)			
										plateau = enlever(choix6,plateau)
										plateau_precedent = retirer(choix6,plateau_precedent)
										plateau = enlever(choix5,plateau)
										plateau_precedent = retirer(choix5,plateau_precedent)		
						else :
							choix4 = 4
							if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix4,tour) == False :
								choix4 = 6
								if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
									choix4 = 7
									plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
									joueur = changer(joueur)
									for c in [1,2,3,4,5,6,7,8,9] :
										choix5 = c
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
											joueur = changer(joueur)
											if choix5 == 1 :
												choix6 = 3
											else :
												choix6 = 1
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 3
											plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
											joueur = changer(joueur)
											for d in [1,2,3,4,5,6,7,8,9] :
												choix7 = d
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
													joueur = changer(joueur)	
													choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
													plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
													joueur = changer(joueur)
													for e in [1,2,3,4,5,6,7,8,9] :
														choix9 = e
														plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
														if plateau != plateau_precedent :
															plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
													plateau = enlever(choix8,plateau)
													plateau_precedent = retirer(choix8,plateau_precedent)
													plateau = enlever(choix7,plateau)
													plateau_precedent = retirer(choix7,plateau_precedent)			
											plateau = enlever(choix6,plateau)
											plateau_precedent = retirer(choix6,plateau_precedent)
											plateau = enlever(choix5,plateau)
											plateau_precedent = retirer(choix5,plateau_precedent)
								else :
									plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
									joueur = changer(joueur)
									for c in [1,2,3,4,5,6,7,8,9] :
										choix5 = c
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
											joueur = changer(joueur)
											if choix5 == 7 :
												choix6 = 5
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 8
											else :
												choix6 = 7
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 5
													if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) == False :
														choix6 = 8
											plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
											joueur = changer(joueur)
											for d in [1,2,3,4,5,6,7,8,9] :
												choix7 = d
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
													joueur = changer(joueur)	
													choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
													plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
													joueur = changer(joueur)
													for e in [1,2,3,4,5,6,7,8,9] :
														choix9 = e
														plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
														if plateau != plateau_precedent :
															plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
													plateau = enlever(choix8,plateau)
													plateau_precedent = retirer(choix8,plateau_precedent)
													plateau = enlever(choix7,plateau)
													plateau_precedent = retirer(choix7,plateau_precedent)			
											plateau = enlever(choix6,plateau)
											plateau_precedent = retirer(choix6,plateau_precedent)
											plateau = enlever(choix5,plateau)
											plateau_precedent = retirer(choix5,plateau_precedent)
							else :
								plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix4,tour)
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
								joueur = changer(joueur)
								for c in [1,2,3,4,5,6,7,8,9] :
									choix5 = c
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
										joueur = changer(joueur)
										if choix5 == 9 :
											choix6 = 6
											if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
												choix6 = 8
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 5
										else :
											choix6 = 9
											if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
												choix6 = 8
												if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
													choix6 = 6
													if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix6,tour) == False :
														choix6 = 5
										plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix6,tour)
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
										joueur = changer(joueur)
										for d in [1,2,3,4,5,6,7,8,9] :
											choix7 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
												joueur = changer(joueur)	
												choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour)
												plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix8,tour)
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												joueur = changer(joueur)
												for e in [1,2,3,4,5,6,7,8,9] :
													choix9 = e
													plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,tour)
													if plateau != plateau_precedent :
														plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
												plateau = enlever(choix8,plateau)
												plateau_precedent = retirer(choix8,plateau_precedent)
												plateau = enlever(choix7,plateau)
												plateau_precedent = retirer(choix7,plateau_precedent)			
										plateau = enlever(choix6,plateau)
										plateau_precedent = retirer(choix6,plateau_precedent)
										plateau = enlever(choix5,plateau)
										plateau_precedent = retirer(choix5,plateau_precedent)
							plateau = enlever(choix4,plateau)
							plateau_precedent = retirer(choix4,plateau_precedent)
							plateau = enlever(choix3,plateau)
							plateau_precedent = retirer(choix3,plateau_precedent)
				plateau = enlever(choix2,plateau)
				plateau_precedent = retirer(choix2,plateau_precedent)
				plateau = enlever(choix1,plateau)
				plateau_precedent = retirer(choix1,plateau_precedent)
	#'''
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 718 et 778
	# Enlevez les # des lignes 353 et 714
	'''
	premier_joueur == "IA"						
	if premier_joueur == "IA" :
		choix1 = 5
		plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix1,tour,dejavu)
		plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
		joueur = changer(joueur)
		for a in [1,2,3,4,5,6,7,8,9] :
			choix2 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2,tour)
			if plateau != plateau_precedent :
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
				joueur = changer(joueur)		
				choix3 = choix_miroir(choix)
				plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix3,tour,dejavu)
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
				joueur = changer(joueur)
				for b in [1,2,3,4,5,6,7,8,9] :
					choix4 = b
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4,tour)
					if plateau != plateau_precedent :
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
						joueur = changer(joueur)		
						choix5 = choix_miroir(choix)
						plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix5,tour,dejavu)
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
						joueur = changer(joueur)
						for c in [1,2,3,4,5,6,7,8,9] :
							choix6 = c
							plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6,tour)
							if plateau != plateau_precedent :
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6d)
								joueur = changer(joueur)	
								choix7 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour,dejavu)
								plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix7,tour,dejavu)
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
								for d in [1,2,3,4,5,6,7,8,9] :
									choix8 = d
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8,tour)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
										joueur = changer(joueur)	
										choix9 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,tour,dejavu)
										plateau = placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix9,tour,dejavu)
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
										plateau = enlever(choix8,plateau)
										plateau_precedent = enlever(choix8,plateau_precedent)	
										joueur = changer(joueur)			
								plateau = enlever(choix7,plateau)
								plateau_precedent = enlever(choix7,plateau_precedent)
								plateau = enlever(choix6,plateau)
								plateau_precedent = enlever(choix6,plateau_precedent)		
						plateau = enlever(choix5,plateau)
						plateau_precedent = enlever(choix5,plateau_precedent)
						plateau = enlever(choix4,plateau)
						plateau_precedent = enlever(choix4,plateau_precedent)
				plateau = enlever(choix3,plateau)
				plateau_precedent = enlever(choix3,plateau_precedent)
				plateau = enlever(choix2,plateau)
				plateau_precedent = enlever(choix2,plateau_precedent)
	'''
				
morpion()		
