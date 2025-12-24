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
def placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,tour) :
	
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
def estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,tour) :
		
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		return False
	if joueur == "IA" :		
		choix = obligation(tour,plateau,symbole,joueur,premier_joueur)
		if choix in range (1,10) :
			return True
		if empecheVictoire(premier_joueur,symbole,choix,plateau) == True :
			return False	
	
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
	
def empecheVictoire(premier_joueur,symbole,choix,plateau) :
	
	if premier_joueur == "joueur" and symbole == "X" or premier_joueur == "IA" and symbole == "X" :
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
	if premier_joueur == "joueur" and symbole == "O" or premier_joueur == "IA" and symbole == "O" :			
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
			
def obligation(tour,plateau,symbole,joueur,premier_joueur) :
		
	dejavu = []
	ligne = 0
	colonne = 0
	essais = 0
	choix = 0
	if tour == 8 :
		while essais < 3 :
			plateau_choix_dejavu = remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
			plateau = plateau_choix_dejavu[0]
			choix = plateau_choix_dejavu[1]
			dejavu = plateau_choix_dejavu[2]
			if estVictorieux(plateau) == True :
				essais += 1
				coordonnees = traduction_choix(choix)
				ligne = coordonnees[0]
				colonne = coordonnees[1]
				plateau = enlever(choix,plateau)
				if essais == 2 :
					dejavu = []
					plateau_choix_dejavu = remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
					choix = plateau_choix_dejavu[1]
					plateau = enlever(choix,plateau)
					break
			else :
				dejavu = []
				plateau = enlever(choix,plateau)
				break
	return choix
	
def remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau) :
	
	choix = 0
	if tour == 8 :	
		if (premier_joueur == "joueur" and symbole == "X" or premier_joueur == "IA" and symbole == "X") :					
			while choix == 0 :
				if plateau[0][0] == 1 :
					if 1 not in dejavu :
						plateau[0][0] = "O"
						dejavu.append(1)
						choix = 1
						break
				if plateau[0][1] == 2 :
					if 2 not in dejavu :
						plateau[0][1] = "O"
						dejavu.append(2)
						choix = 2
						break
				if plateau[0][2] == 3 :
					if 3 not in dejavu :
						plateau[0][2] = "O"
						dejavu.append(3)
						choix = 3
						break
				if plateau[1][0] == 4 :
					if 4 not in dejavu :
						plateau[1][0] = "O"
						dejavu.append(4)
						choix = 4
						break
				if plateau[1][1] == 5 :
					if 5 not in dejavu :
						plateau[1][1] = "O"
						dejavu.append(5)
						choix = 5
						break
				if plateau[1][2] == 6 :
					if 6 not in dejavu :
						plateau[1][2] = "O"
						dejavu.append(6)
						choix = 6
						break
				if plateau[2][0] == 7 :
					if 7 not in dejavu :
						plateau[2][0] = "O"
						dejavu.append(7)
						choix = 7
						break
				if plateau[2][1] == 8 :
					if 8 not in dejavu :
						plateau[2][1] = "O"
						dejavu.append(8)
						choix = 8
						break
				if plateau[2][2] == 9 :
					if 9 not in dejavu :
						plateau[2][2] = "O"
						dejavu.append(9)
						choix = 9
						break
		if (premier_joueur == "joueur" and symbole == "O" or premier_joueur == "IA" and symbole == "O") :		
			while choix == 0 :
				if plateau[0][0] == 1 :
					if 1 not in dejavu :
						plateau[0][0] = "X"
						dejavu.append(1)
						choix = 1
						break
				if plateau[0][1] == 2 :
					if 2 not in dejavu :
						plateau[0][1] = "X"
						dejavu.append(2)
						choix = 2
						break
				if plateau[0][2] == 3 :
					if 3 not in dejavu :
						plateau[0][2] = "X"
						dejavu.append(3)
						choix = 3
						break
				if plateau[1][0] == 4 :
					if 4 not in dejavu :
						plateau[1][0] = "X"
						dejavu.append(4)
						choix = 4
						break
				if plateau[1][1] == 5 :
					if 5 not in dejavu :
						plateau[1][1] = "X"
						dejavu.append(5)
						choix = 5
						break
				if plateau[1][2] == 6 :
					if 6 not in dejavu :
						plateau[1][2] = "X"
						dejavu.append(6)
						choix = 6
						break
				if plateau[2][0] == 7 :
					if 7 not in dejavu :
						plateau[2][0] = "X"
						dejavu.append(7)
						choix = 7
						break
				if plateau[2][1] == 8 :
					if 8 not in dejavu :
						plateau[2][1] = "X"
						dejavu.append(8)
						choix = 8
						break
				if plateau[2][2] == 9 :
					if 9 not in dejavu :
						plateau[2][2] = "X"
						dejavu.append(9)
						choix = 9
						break
	plateau_choix_dejavu = [plateau,choix,dejavu]
	return plateau_choix_dejavu					

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

def decision(plateau,joueur,premier_joueur,symbole,choix,tour) :
	
	erreur = 1
	choix = obligation(plateau,symbole,joueur,premier_joueur,choix)
	if choix not in range (1,10) :
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
		
	print("Test IA morpion aleatoire")
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	premier_joueur = "joueur"
	joueur = "joueur"
	dejavu = []
	tour = 1
	# Si vous voulez essayer la partie où le joueur 1 a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 450 et 452
	# Enlevez les # des lignes 456 et 458
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer la partie où le joueur 1 a choisi les X et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 456 et 458
	# Enlevez les # des lignes 450 et 452
	'''
	symbole = "X"
	'''	
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 462 et 540
	# Enlevez les # des lignes 544 et 623
	#'''
	if premier_joueur == "joueur" :
		for a in [1,2,3,4,5,6,7,8,9] :
			choix1 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1,tour)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
			joueur = changer(joueur)
			choix2 = decision(plateau,joueur,premier_joueur,symbole,choix,tour)
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2,tour)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
			joueur = changer(joueur)
			for b in [1,2,3,4,5,6,7,8,9] :
				choix3 = b
				plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3,tour)
				if plateau != plateau_precedent :
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
					joueur = changer(joueur)
					choix4 = decision(plateau,joueur,premier_joueur,symbole,choix,tour)
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4,tour)
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
					joueur = changer(joueur)
					for c in [1,2,3,4,5,6,7,8,9] :
						choix5 = c
						plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,tour)
						if plateau != plateau_precedent :
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
							joueur = changer(joueur)
							choix6 = decision(plateau,joueur,premier_joueur,symbole,choix,tour)
							plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6,tour)
							if plateau != plateau_precedent :
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
								joueur = changer(joueur)
								for d in [1,2,3,4,5,6,7,8,9] :
									choix7 = d
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,tour)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
										joueur = changer(joueur)
										tour = 8
										choix8 = decision(plateau,joueur,premier_joueur,symbole,choix,tour)
										tour = 7
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8,tour)
										if plateau != plateau_precedent :
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
										else :
											plateau = enlever(choix8,plateau)
											plateau_precedent = retirer(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = retirer(choix7,plateau_precedent)	
											joueur = changer(joueur)			
								plateau = enlever(choix6,plateau)
								plateau_precedent = retirer(choix6,plateau_precedent)
								plateau = enlever(choix5,plateau)
								plateau_precedent = retirer(choix5,plateau_precedent)
							else :	
								plateau = enlever(choix6,plateau)
								plateau_precedent = retirer(choix6,plateau_precedent)
								plateau = enlever(choix5,plateau)
								plateau_precedent = retirer(choix5,plateau_precedent)
								joueur = changer(joueur)
					plateau = enlever(choix4,plateau)
					plateau_precedent = retirer(choix4,plateau_precedent)
					plateau = enlever(choix3,plateau)
					plateau_precedent = retirer(choix3,plateau_precedent)
			plateau = enlever(choix2,plateau)
			plateau_precedent = retirer(choix2,plateau_precedent)
			plateau = enlever(choix1,plateau)
			plateau_precedent = retirer(choix1,plateau_precedent)
	#'''			
	# Si vous voulez essayer la partie où l'IA commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 544 et 623
	# Enlevez les # des lignes 462 et 540
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
