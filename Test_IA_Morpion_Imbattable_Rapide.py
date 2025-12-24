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
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) :

	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"
	else :
		plateau[ligne][colonne] = "X"
	if joueur == "IA" :
		choix = traduction_coordonnees(ligne,colonne)
		print("L'IA a joué ",choix)
	if joueur == "joueur" :
		print("Vous avez les ",symbole)
	afficher(plateau)
	if estVictorieux(plateau) == True :
		victoire(plateau)
	if estEgalitaire(plateau) == True :
		joueur = remplir(plateau,symbole,joueur,premier_joueur)
		if estVictorieux(plateau) == True :
			victoire(plateau)
		egalite(plateau)

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.	
def enlever(plateau,choix) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix
		
def traduction(choix,joueur,premier_joueur,symbole,plateau) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix)

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

def remplir(plateau,symbole,joueur,premier_joueur) :

	if aLesRonds(joueur,premier_joueur,symbole) == True :
		if plateau[0][0] == 1 :
			plateau[0][0] = "X"
			case = 1
		if plateau[0][1] == 2 :
			plateau[0][1] = "X"
			case = 2
		if plateau[0][2] == 3 :
			plateau[0][2] = "X"
			case = 3
		if plateau[1][0] == 4 :
			plateau[1][0] = "X"
			case = 4
		if plateau[1][1] == 5 :
			plateau[1][1] = "X"
			case = 5
		if plateau[1][2] == 6 :
			plateau[1][2] = "X"
			case = 6
		if plateau[2][0] == 7 :
			plateau[2][0] = "X"
			case = 7
		if plateau[2][1] == 8 :
			plateau[2][1] = "X"
			case = 8
		if plateau[2][2] == 9 :
			plateau[2][2] = "X"
			case = 9
	else :
		if plateau[0][0] == 1 :
			plateau[0][0] = "O"
			case = 1
		if plateau[0][1] == 2 :
			plateau[0][1] = "O"
			case = 2
		if plateau[0][2] == 3 :
			plateau[0][2] = "O"
			case = 3
		if plateau[1][0] == 4 :
			plateau[1][0] = "O"
			case = 4
		if plateau[1][1] == 5 :
			plateau[1][1] = "O"
			case = 5
		if plateau[1][2] == 6 :
			plateau[1][2] = "O"
			case = 6
		if plateau[2][0] == 7 :
			plateau[2][0] = "O"
			case = 7
		if plateau[2][1] == 8 :
			plateau[2][1] = "O"
			case = 8
		if plateau[2][2] == 9 :
			plateau[2][2] = "O"
			case = 9
	joueur = changer(joueur)
	if joueur == "joueur" :
		print("Remplissage de la dernière case (",case,") pour vous")
	else :
		print("L'IA joue la dernière case")
	afficher(plateau)
	return joueur	

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
	if total == 8 :
		return True		

#Affiche le gagnant en l'informant de sa victoire.	
def victoire(plateau) :
	
	print("L'IA a gagné")

#Affiche qu'il y a égalité.	
def egalite(plateau) :
	
	print("Il y a égalité.")

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.
def changer(joueur) :

	if joueur == "IA" :
		joueur = "joueur"
	else :
		joueur = "IA" 
	return joueur
	
def morpion() :
	
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	joueur = "joueur"
	premier_joueur = "joueur"
	reponse = "O"
	symbole_possible = ["O","X"]
	print("IA morpion imbattable rapide")
	for symbole_choisi in symbole_possible :
		symbole = symbole_choisi
		afficher(plateau)
		if reponse == "O" :
			for i in [1,2,3,4,5,6,7,8,9] :
				choix = i
				if choix == 1 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [2,3,4,6,7,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [6,8,9] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 7
									enlever(plateau,4)
									enlever(plateau,choix)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [6,7,9] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [6,8,9] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,7)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [3,4,7,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [3,4,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [3,8,9] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [2,3,4,7,9] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [2,3,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,6)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [3,4,6,7,8] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [3,4,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									else :
										traduction(choix,joueur,premier_joueur,symbole,plateau)
										placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
										enlever(plateau,choix)
										enlever(plateau,8)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 1
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 2 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,3,4,6,7,8,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [6,8,9] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,9)
											enlever(plateau,8)
											enlever(plateau,choix)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,8)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [1,6,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [6,8,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [3,4,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,3,6,8,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [3,8,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [3,4,6,7,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [3,4,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,3,6,7,8] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [1,7,8] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,4)
					choix = 2
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 3 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,4,6,7,8,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [6,7,9] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [4,6,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,8)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [1,2,6,7,9] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [6,7,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,8)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 1 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 1
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									enlever(plateau,choix)
									enlever(plateau,1)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,9)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,4,6,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,4,6] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,2,6,7,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,2,7] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [1,7,8] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,6)
					choix = 3
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 4 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,3,6,7,8,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [6,8,9] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,7)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [3,6,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [6,7,8] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,6,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [2,7,8] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,8)
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,2)
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,2)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,3,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [2,7,8] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,3,6,7,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 9 
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,3,6,7,8] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [1,3,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 4
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 5 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					for i in [2,3,4,6,7,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [3,4,6,7,9] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [4,6,9] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,7)
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,9)
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,7)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,6)
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,4)
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [4,6,9] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,9)
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,6)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,3)
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [3,6,7] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,8)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [2,4,6,8,9] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [2,8,9] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,9)
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,8)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,7)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [2,3,7,8,9] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,9)
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,7)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,8)
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [2,8,9] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,9)
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,8)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,7)
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [2,8,9] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,3)
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,2)
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [3,7,8] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,8)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,6)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [2,3,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [2,8,9] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [2,4,6,8,9] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [4,6,9] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,9)
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,6)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [3,4,6,7,9] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [4,6,9] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [2,4,6,7,8] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [4,6,7] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,7)
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,7)
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,6)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,3)
					choix = 5
					enlever(plateau,choix)
					enlever(plateau,1)
				if choix == 6 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,3,4,7,8,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [2,3,4,7,9] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [4,7,9] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,8)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [3,4,7,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 1 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [4,7,8] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 1
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									enlever(plateau,choix)
									enlever(plateau,1)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,9)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,3,7,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,3,4,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,3,4] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [1,2,4,7,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,2,4] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [1,2,4] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,3)
					choix = 6
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 7 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,3,4,6,8,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [3,8,9] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [1,3,4,8,9] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [3,8,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,8)
											enlever(plateau,3)
											enlever(plateau,choix)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,6)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,4,6,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,4,6] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,3,6,8,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,6)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									enlever(plateau,choix)
									enlever(plateau,8)
									choix = 9
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,3,4,8,9] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,3,4] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,3)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 1 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 1
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									enlever(plateau,choix)
									enlever(plateau,1)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,9)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [1,3,6] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,8)
					choix = 7
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 8 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,3,4,6,7,9] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [2,3,4,7,9] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [2,3,9] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,9)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,6)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,3,6,7,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									for i in [3,7,9] :
										choix = i
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,1)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,2,6,7,9] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,2,7] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
											enlever(plateau,7)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
							for i in [2,3,6,7,9] :
								choix = i
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,1)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [1,2,4,7,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									for i in [1,2,4,7,9] :
										choix = i
										if choix == 1 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
									choix = 7
									enlever(plateau,7)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 1 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [2,3,6] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)											 
									choix = 1
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
									enlever(plateau,choix)
									enlever(plateau,1)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,9)
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [1,2,4] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,7)
					choix = 8
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 9 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [1,2,3,4,6,7,8] :
						choix = i
						if choix == 1 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [3,4,6,7,8] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [3,4,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 1
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [1,3,6,7,8] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									for i in [1,7,8] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,3)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,4)
						if choix == 3 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									for i in [1,7,8] :
										choix = i
										if choix == 8 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
											enlever(plateau,choix)
											enlever(plateau,8)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,2)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,4)									 
							choix = 3
							enlever(plateau,choix)
							enlever(plateau,6)
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							for i in [1,3,6,7,8] :
								choix = i
								if choix == 8 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									for i in [1,3,6] :
										choix = i
										if choix == 3 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
									choix = 8
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,2)
						if choix == 6 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
							for i in [1,2,4,7,8] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									for i in [1,2,4] :
										choix = i
										if choix == 2 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
											enlever(plateau,4)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
											enlever(plateau,choix)
											enlever(plateau,2)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 6
							enlever(plateau,choix)
							enlever(plateau,3)
						if choix == 7 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 2 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [1,3,6] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
											enlever(plateau,choix)
											enlever(plateau,3)
											enlever(plateau,1)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 2
									enlever(plateau,choix)
									enlever(plateau,4)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
									enlever(plateau,choix)
									enlever(plateau,2)
							choix = 7
							enlever(plateau,choix)
							enlever(plateau,8)
						if choix == 8 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [1,2,3,4,6] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [1,2,4] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
											enlever(plateau,choix)
											enlever(plateau,1)
											enlever(plateau,2)
										else :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 3
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 8
							enlever(plateau,choix)
							enlever(plateau,7)
					choix = 9
					enlever(plateau,choix)
					enlever(plateau,5)
			reponse = "N"
		if reponse == "N" :
			premier_joueur = "IA"
			placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			for i in [2,3,4,5,6,7,8,9] :
				choix = i
				if choix == 2 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
					for i in [3,4,6,7,8,9] :
						choix = i
						if choix == 9 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							for i in [3,6,7,8] :
								choix = i
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
							choix = 9
							enlever(plateau,choix)
							enlever(plateau,4)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							enlever(plateau,choix)
							enlever(plateau,9)
					choix = 2
					enlever(plateau,choix)
					enlever(plateau,5)
				if choix == 3 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					for i in [2,4,5,6,8,9] :
						choix = i
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [2,5,6,8] :
								choix = i
								if choix == 5 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
									enlever(plateau,choix)
									enlever(plateau,8)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
									enlever(plateau,choix)
									enlever(plateau,5)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,9)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							enlever(plateau,choix)
							enlever(plateau,4)
					choix = 3
					enlever(plateau,choix)
					enlever(plateau,7)
				if choix == 4 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					for i in [2,5,6,7,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
							for i in [6,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,5)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 4
					enlever(plateau,choix)
					enlever(plateau,3)
				if choix == 5 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					for i in [2,4,6,7,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
							for i in [4,6,7,9] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [7,9] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 4
									enlever(plateau,choix)
									enlever(plateau,6)
								if choix == 6 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [7,9] :
										choix = i
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
									choix = 6
									enlever(plateau,choix)
									enlever(plateau,4)
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									for i in [4,9] :
										choix = i
										if choix == 4 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
											enlever(plateau,choix)
											enlever(plateau,9)
										if choix == 9 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
											enlever(plateau,choix)
											enlever(plateau,4)
									choix = 7
									enlever(plateau,choix)
									enlever(plateau,6)
								if choix == 9 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									for i in [6,7] :
										choix = i
										if choix == 6 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
											enlever(plateau,choix)
											enlever(plateau,7)
										if choix == 7 :
											traduction(choix,joueur,premier_joueur,symbole,plateau)
											placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
											enlever(plateau,choix)
											enlever(plateau,6)
									choix = 9
									enlever(plateau,choix)
									enlever(plateau,4)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,8)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 5
					enlever(plateau,choix)
					enlever(plateau,3)
				if choix == 6 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					for i in [2,4,5,7,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
							for i in [4,7,8,9] :
								choix = i
								if choix == 7 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
									enlever(plateau,choix)
									enlever(plateau,7)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,5)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 6
					enlever(plateau,choix)
					enlever(plateau,3)
				if choix == 7 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					for i in [2,4,5,6,8,9] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
							for i in [4,5,6,8] :
								choix = i
								if choix == 5 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
									enlever(plateau,choix)
									enlever(plateau,6)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
									enlever(plateau,choix)
									enlever(plateau,5)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,9)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							enlever(plateau,choix)
							enlever(plateau,2)
					choix = 7
					enlever(plateau,choix)
					enlever(plateau,3)
				if choix == 8 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					for i in [2,3,4,5,6,9] :
						choix = i
						if choix == 4 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
							for i in [2,3,6,9] :
								choix = i
								if choix == 3 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
									enlever(plateau,choix)
									enlever(plateau,9)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
									enlever(plateau,choix)
									enlever(plateau,3)
							choix = 4
							enlever(plateau,choix)
							enlever(plateau,5)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
							enlever(plateau,choix)
							enlever(plateau,4)
					choix = 8
					enlever(plateau,choix)
					enlever(plateau,7)
				if choix == 9 :
					traduction(choix,joueur,premier_joueur,symbole,plateau)
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					for i in [2,4,5,6,7,8] :
						choix = i
						if choix == 2 :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
							for i in [4,5,6,8] :
								choix = i
								if choix == 4 :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
									enlever(plateau,choix)
									enlever(plateau,5)
								else :
									traduction(choix,joueur,premier_joueur,symbole,plateau)
									placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
									enlever(plateau,choix)
									enlever(plateau,5)
							choix = 2
							enlever(plateau,choix)
							enlever(plateau,7)
						else :
							traduction(choix,joueur,premier_joueur,symbole,plateau)
							placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
							enlever(plateau,choix)
							enlever(plateau,2)
morpion()

