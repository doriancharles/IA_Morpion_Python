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
def placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"
	else :
		plateau[ligne][colonne] = "X"
	if estVictorieux(plateau) == True :		
		victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)	
		plateau = enlever(choix,plateau)
		plateau_precedent = enlever(choix,plateau_precedent)
	if estEgalitaire(plateau) == True :		
		if estVictorieux(plateau) == True :			
			victoire_joueur(plateau)	
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)		
		else : 
			egalite(plateau,liste_Coups)
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

#Traduit un choix en coordonnées (ligne et colonne).	
#Si la méthode "estPossible" n'a pas retourné Faux, il utilise la méthode "placer_valeur"
#Si la méthode "estVictorieux" retourne True, il utilise les méthodes "victoire_joueur", "enlever"
def traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix,liste_Coups,liste_Coups_Gagnant) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) != False :
		placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant)
	if estVictorieux(plateau) == True :					
		victoire_joueur(plateau)	
		enlever(plateau,choix)
		retirer(choix,plateau_precedent)	
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
	
def victoire_joueur(plateau) :
	
	afficher(plateau)
	print("Vous avez gagné, joueur")

#Affiche le gagnant en l'informant de sa victoire.
def victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant) :
			
	afficher(plateau)	
	if joueur == "joueur" :	
		print("Vous avez gagné.")	
		liste_Coups.append(choix)
		choix_change = liste_Coups[len(liste_Coups)-1]
		liste_Coups.pop()
		liste_Coups[len(liste_Coups)-1] = choix_change
		liste_Coups_Gagnant.append(liste_Coups)	
		morpion(liste_Coups_Gagnant)
	else :				
		print("L'IA a gagné")					
	
#Affiche qu'il y a égalité.		
def egalite(plateau,liste_Coups) :
		
	afficher(plateau)
	liste_Coups.pop()
	liste_Coups.pop()
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

def decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant) :
	
	changement = 0
	if liste_Coups_Gagnant != [] :
		for i in range (len(liste_Coups_Gagnant)) :
			liste_Test = liste_Coups_Gagnant[i]
			choix = liste_Test[len(liste_Test)-1]
			liste_Test.pop()
			if liste_Coups == liste_Test :
				changement = 1
			liste_Test.append(choix)
			if changement == 1 :
				break
	if changement != 1 :
		choix = remplir(plateau,symbole,joueur,premier_joueur)
	liste_Coups.append(choix)
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	placer_valeur(joueur,premier_joueur,symbole,plateau,plateau_precedent,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant)
	if estVictorieux(plateau) == True :		
		victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)	
		plateau = enlever(choix,plateau)
		plateau_precedent = enlever(choix,plateau_precedent)
	if estEgalitaire(plateau) == True :		
		if estVictorieux(plateau) == True :			
			victoire_joueur(plateau)	
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)		
		else : 
			egalite(plateau,liste_Coups)
			plateau = enlever(choix,plateau)
			plateau_precedent = enlever(choix,plateau_precedent)	
	return choix

def remplir(plateau,symbole,joueur,premier_joueur) :
	
	decision = 0
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		while decision == 0 :
			if plateau[0][0] == 1 :
				plateau[0][0] = "O"
				choix = 1
				break
			if plateau[0][1] == 2 :
				plateau[0][1] = "O"
				choix = 2
				break	
			if plateau[0][2] == 3 :	
				plateau[0][2] = "O"	
				choix = 3
				break
			if plateau[1][0] == 4 :	
				plateau[1][0] = "O"	
				choix = 4
				break
			if plateau[1][1] == 5 :	
				plateau[1][1] = "O"
				choix = 5	
				break
			if plateau[1][2] == 6 :
				plateau[1][2] = "O"	
				choix = 6
				break
			if plateau[2][0] == 7 :	
				plateau[2][0] = "O"
				choix = 7
				break	
			if plateau[2][1] == 8 :	
				plateau[2][1] = "O"	
				choix = 8
				break
			if plateau[2][2] == 9 :	
				plateau[2][2] = "O"	
				choix = 9
				break
	else :
		while decision == 0 :
			if plateau[0][0] == 1 :	
				plateau[0][0] = "X"	
				choix = 1
				break					
			if plateau[0][1] == 2 :						
				plateau[0][1] = "X"	
				choix = 2
				break					
			if plateau[0][2] == 3 :						
				plateau[0][2] = "X"	
				choix = 3
				break					
			if plateau[1][0] == 4 :					
				plateau[1][0] = "X"
				choix = 4
				break						
			if plateau[1][1] == 5 :						
				plateau[1][1] = "X"	
				choix = 5
				break		
			if plateau[1][2] == 6 :
				plateau[1][2] = "X"	
				choix = 6
				break
			if plateau[2][0] == 7 :	
				plateau[2][0] = "X"
				choix = 7
				break
			if plateau[2][1] == 8 :
				plateau[2][1] = "X"
				choix = 8
				break
			if plateau[2][2] == 9 :
				plateau[2][2] = "X"	
				choix = 9
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

def morpion(liste_Coups_Gagnant) :
		
	liste_Coups = []
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	premier_joueur = "joueur"
	joueur = "joueur"
	# Si vous voulez essayer la partie où le joueur 1 a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 321 et 323
	# Enlevez les # des lignes 327 et 329
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer la partie où le joueur 1 a choisi les X et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 327 et 329
	# Enlevez les # des lignes 321 et 323
	'''
	symbole = "X"
	'''	
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 333 et 412
	# Enlevez les # des lignes 544 et 623
	#'''			
	if premier_joueur == "joueur" :	
		for a in [1,2,3,4,5,6,7,8,9] :
			choix1 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1,liste_Coups,liste_Coups_Gagnant)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
			liste_Coups.append(choix1)
			joueur = changer(joueur)
			choix2 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2,liste_Coups,liste_Coups_Gagnant)
			plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
			joueur = changer(joueur)
			for b in [1,2,3,4,5,6,7,8,9] :
				choix3 = b
				plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3,liste_Coups,liste_Coups_Gagnant)
				if plateau != plateau_precedent :
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
					liste_Coups.append(choix3)
					joueur = changer(joueur)
					choix4 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4,liste_Coups,liste_Coups_Gagnant)
					plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
					joueur = changer(joueur)
					for c in [1,2,3,4,5,6,7,8,9] :
						choix5 = c
						plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,liste_Coups,liste_Coups_Gagnant)
						if plateau != plateau_precedent :
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
							liste_Coups.append(choix5)
							joueur = changer(joueur)
							choix6 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
							plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6,liste_Coups,liste_Coups_Gagnant)
							if plateau != plateau_precedent :
								plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
								joueur = changer(joueur)
								for d in [1,2,3,4,5,6,7,8,9] :
									choix7 = d
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,liste_Coups,liste_Coups_Gagnant)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
										liste_Coups.append(choix7)
										joueur = changer(joueur)
										choix8 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
										plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8,liste_Coups,liste_Coups_Gagnant)
										if plateau != plateau_precedent :
											plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
											joueur = changer(joueur)
											for e in [1,2,3,4,5,6,7,8,9] :
												choix9 = e
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,liste_Coups,liste_Coups_Gagnant)
												if plateau != plateau_precedent :
													plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix9)
													print(liste_Coups)
											plateau = enlever(choix8,plateau)
											plateau_precedent = enlever(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = enlever(choix7,plateau_precedent)
										else :
											plateau = enlever(choix8,plateau)
											plateau_precedent = enlever(choix8,plateau_precedent)
											plateau = enlever(choix7,plateau)
											plateau_precedent = enlever(choix7,plateau_precedent)				
								plateau = enlever(choix6,plateau)
								plateau_precedent = enlever(choix6,plateau_precedent)
								plateau = enlever(choix5,plateau)
								plateau_precedent = enlever(choix5,plateau_precedent)
							else :	
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
			plateau = enlever(choix1,plateau)
			plateau_precedent = enlever(choix1,plateau_precedent)
	#'''
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 416 et 495
	# Enlevez les # des lignes 333 et 412
	'''		
	premier_joueur = "IA"
	joueur = "IA"
	if premier_joueur == "IA" :	
		choix1 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1,liste_Coups,liste_Coups_Gagnant)
		plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
		joueur = changer(joueur)
		for a in [1,2,3,4,5,6,7,8,9] :
			choix2 = a
			plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix2,liste_Coups,liste_Coups_Gagnant)
			if plateau != plateau_precedent :
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix2)
				liste_Coups.append(choix2)
				joueur = changer(joueur)
				choix3 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
				plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix3,liste_Coups,liste_Coups_Gagnant)
				plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix3)
				joueur = changer(joueur)
				for b in [1,2,3,4,5,6,7,8,9] :
					choix4 = b
					plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix4,liste_Coups,liste_Coups_Gagnant)
					if plateau != plateau_precedent :
						plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix4)
						liste_Coups.append(choix4)
						joueur = changer(joueur)
						choix5 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
						plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix5,liste_Coups,liste_Coups_Gagnant)
						if plateau != plateau_precedent :
							plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix5)
							joueur = changer(joueur)
							for c in [1,2,3,4,5,6,7,8,9] :
								choix6 = c
								plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix6,liste_Coups,liste_Coups_Gagnant)
								if plateau != plateau_precedent :
									plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix6)
									liste_Coups.append(choix5)
									joueur = changer(joueur)
									choix7 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
									plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix7,liste_Coups,liste_Coups_Gagnant)
									if plateau != plateau_precedent :
										plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix7)
										joueur = changer(joueur)
										for d in [1,2,3,4,5,6,7,8,9] :
											choix8 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8,liste_Coups,liste_Coups_Gagnant)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												liste_Coups.append(choix8)
												joueur = changer(joueur)
												choix9 = decision(plateau,plateau_precedent,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9,liste_Coups,liste_Coups_Gagnant)
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
liste_Coups_Gagnant = []					
morpion(liste_Coups_Gagnant)		

