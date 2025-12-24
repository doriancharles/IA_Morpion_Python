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
			victoire(joueur,plateau)	
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

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau) :
	
	afficher(plateau)			
	if joueur == "joueur" :	
		print("Vous avez gagné")				
	else :				
		print("L'IA a gagné")			
	print("")	

#Affiche qu'il y a égalité.	
def egalite(plateau) :
		
	afficher(plateau)
	print("Il y a égalité.")
	print("")	
		
def remplir(plateau,symbole,joueur,premier_joueur) :

	if aLesRonds(joueur,premier_joueur,symbole) == True :
		if plateau[0][0] == 1 :
			plateau[0][0] = "X"
		if plateau[0][1] == 2 :
			plateau[0][1] = "X"
		if plateau[0][2] == 3 :
			plateau[0][2] = "X"
		if plateau[1][0] == 4 :
			plateau[1][0] = "X"
		if plateau[1][1] == 5 :
			plateau[1][1] = "X"
		if plateau[1][2] == 6 :
			plateau[1][2] = "X"
		if plateau[2][0] == 7 :
			plateau[2][0] = "X"
		if plateau[2][1] == 8 :
			plateau[2][1] = "X"
		if plateau[2][2] == 9 :
			plateau[2][2] = "X"
	else :
		if plateau[0][0] == 1 :
			plateau[0][0] = "O"
		if plateau[0][1] == 2 :
			plateau[0][1] = "O"
		if plateau[0][2] == 3 :
			plateau[0][2] = "O"
		if plateau[1][0] == 4 :
			plateau[1][0] = "O"
		if plateau[1][1] == 5 :
			plateau[1][1] = "O"
		if plateau[1][2] == 6 :
			plateau[1][2] = "O"
		if plateau[2][0] == 7 :
			plateau[2][0] = "O"
		if plateau[2][1] == 8 :
			plateau[2][1] = "O"
		if plateau[2][2] == 9 :
			plateau[2][2] = "O"
	print("Le",joueur,"doit jouer cette dernière case")
	print("")
	afficher(plateau)
	return plateau	

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.	
def enlever(choix,plateau) :
	
	coordonnees = traduction_choix(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix
	return plateau

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.	
def changer(joueur) :
	
	if joueur == "IA" :
		joueur = "joueur"
	else :
		joueur = "IA" 
	return joueur
	
def decision(plateau,joueur,premier_joueur,symbole) :
	
	choix = 0
	if premier_joueur == "joueur" and symbole == "O" :
		if plateau == [["O",2,3],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [["O","O",3],[4,"X",6],[7,8,9]] :
			choix = 3
		if plateau == [["O","O","X"],["O","X",6],[7,8,9]] :
			choix = 7
		if plateau == [["O","O","X"],[4,"X","O"],[7,8,9]] :
			choix = 7
		if plateau == [["O","O","X"],[4,"X",6],["O",8,9]] :
			choix = 4
		if plateau == [["O","O","X"],["X","X","O"],["O",8,9]] :
			choix = 9
		if plateau == [["O","O","X"],["X","X",6],["O","O",9]] :
			choix = 6
		if plateau == [["O","O","X"],["X","X",6],["O",8,"O"]] :
			choix = 6
		if plateau == [["O","O","X"],["O","X","O"],["O",8,9]] :
			choix = 9
		if plateau == [["O","O","X"],[4,"X",6],[7,"O",9]] :
			choix = 7
		if plateau == [["O","O","X"],[4,"X",6],[7,8,"O"]] :
			choix = 7	
		if plateau == [["O",2,"O"],[4,"X",6],[7,8,9]] :
			choix = 2
		if plateau == [["O","X","O"],["O","X",6],[7,8,9]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"X","O"],[7,8,9]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"X",6],["O",8,9]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"X",6],[7,"O",9]] :
			choix = 4
		if plateau == [["O","X","O"],["X","X","O"],[7,"O",9]] :
			choix = 9 
		if plateau == [["O","X","O"],["X","X",6],["O","O",9]] :
			choix = 6
		if plateau == [["O","X","O"],["X","X",6],[7,"O","O"]] :
			choix = 6
		if plateau == [["O","X","O"],["X","X",6],[7,8,"O"]] :
			choix = 8	
		if plateau == [["O",2,3],["O","X",6],[7,8,9]] :
			choix = 7
		if plateau == [["O","O",3],["O","X",6],["X",8,9]] :
			choix = 3
		if plateau == [["O",2,"O"],["O","X",6],["X",8,9]] :
			choix = 2
		if plateau == [["O","X","O"],["O","X","O"],["X",8,9]] :
			choix = 8
		if plateau == [["O","X","O"],["O","X",6],["X","O",9]] :
			choix = 9
		if plateau == [["O","X","O"],["O","X",6],["X",8,"O"]] :
			choix = 8
		if plateau == [["O",2,3],["O","X","O"],["X",8,9]] :
			choix = 3
		if plateau == [["O",2,3],["O","X",6],["X","O",9]] :
			choix = 3
		if plateau == [["O",2,3],["O","X",6],["X",8,"O"]] :
			choix = 3
		if plateau == [["O",2,3],[4,"X","O"],[7,8,9]] :
			choix = 2
		if plateau == [["O","X",3],["O","X","O"],[7,8,9]] :
			choix = 8
		if plateau == [["O","X",3],[4,"X","O"],["O",8,9]] :
			choix = 8
		if plateau == [["O","X",3],[4,"X","O"],[7,"O",9]] :
			choix = 7
		if plateau == [["O","X","O"],[4,"X","O"],["X","O",9]] :
			choix = 9
		if plateau == [["O","X",3],["O","X","O"],["X","O",9]] :
			choix = 3
		if plateau == [["O","X",3],[4,"X","O"],["X","O","O"]] :
			choix = 3
		if plateau == [["O","X",3],[4,"X","O"],[7,8,"O"]] :
			choix = 8
		if plateau == [["O",2,3],[4,"X",6],["O",8,9]] :
			choix = 4
		if plateau == [["O","O",3],["X","X",6],["O",8,9]] :
			choix = 6
		if plateau == [["O",2,"O"],["X","X",6],["O",8,9]] :
			choix = 6
		if plateau == [["O",2,3],["X","X","O"],["O",8,9]] :
			choix = 2
		if plateau == [["O","X","O"],["X","X","O"],["O",8,9]] :
			choix = 8
		if plateau == [["O","X",3],["X","X","O"],["O","O",9]] :
			choix = 9
		if plateau == [["O","X",3],["X","X","O"],["O",8,"O"]] :
			choix = 8
		if plateau == [["O",2,3],["X","X",6],["O","O",9]] :
			choix = 6
		if plateau == [["O",2,3],["X","X",6],["O",8,"O"]] :
			choix = 6
		if plateau == [["O",2,3],[4,"X",6],[7,"O",9]] :
			choix = 6
		if plateau == [["O","O",3],[4,"X","X"],[7,"O",9]] :
			choix = 4
		if plateau == [["O",2,"O"],[4,"X","X"],[7,"O",9]] :
			choix = 4
		if plateau == [["O",2,3],["O","X","X"],[7,"O",9]] :
			choix = 7
		if plateau == [["O","O",3],["O","X","X"],["X","O",9]] :
			choix = 3
		if plateau == [["O",2,"O"],["O","X","X"],["X","O",9]] :
			choix = 2
		if plateau == [["O",2,3],["O","X","X"],["X","O","O"]] :
			choix = 3
		if plateau == [["O",2,3],[4,"X","X"],["O","O",9]] :
			choix = 4
		if plateau == [["O",2,3],[4,"X","X"],[7,"O","O"]] :
			choix = 4	
		if plateau == [["O",2,3],[4,"X",6],[7,8,"O"]] :
			choix = 2
		if plateau == [["O","X","O"],[4,"X",6],[7,8,"O"]] :
			choix = 8
		if plateau == [["O","X",3],["O","X",6],[7,8,"O"]] :
			choix = 8
		if plateau == [["O","X",3],[4,"X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["O","X",3],[4,"X",6],[7,"O","O"]] :
			choix = 7
		if plateau == [["O","X","O"],[4,"X",6],["X","O","O"]] :
			choix = 6
		if plateau == [["O","X",3],["O","X",6],["X","O","O"]] :
			choix = 3
		if plateau == [[1,"O",3],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,"O","O"],[4,"X",6],[7,8,9]] :
			choix = 1
		if plateau == [["X","O","O"],["O","X",6],[7,8,9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"X","O"],[7,8,9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"X",6],["O",8,9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"X",6],[7,"O",9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"X",6],[7,8,"O"]] :
			choix = 6
		if plateau == [["X","O","O"],["O","X","X"],[7,8,"O"]] :
			choix = 7
		if plateau == [["X","O","O"],[4,"X","X"],["O",8,"O"]] :
			choix = 4
		if plateau == [["X","O","O"],[4,"X","X"],[7,"O","O"]] :
			choix = 4
		if plateau == [[1,"O",3],["O","X",6],[7,8,9]] :
			choix = 1
		if plateau == [["X","O",3],["O","X","O"],[7,8,9]] :
			choix = 9
		if plateau == [["X","O",3],["O","X",6],["O",8,9]] :
			choix = 9
		if plateau == [["X","O",3],["O","X",6],[7,"O",9]] :
			choix = 9
		if plateau == [["X","O",3],["O","X",6],[7,8,"O"]] :
			choix = 3
		if plateau == [["X","O","X"],["O","X","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [["X","O","X"],["O","X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["X","O","X"],["O","X",6],["O",8,"O"]] :
			choix = 6
		if plateau == [["X","O","X"],["O","X",6],[7,"O","O"]] :
			choix = 7		
		if plateau == [[1,"O",3],[4,"X","O"],[7,8,9]] :
			choix = 1
		if plateau == [["X","O",3],[4,"X","O"],["O",8,9]] :
			choix = 9
		if plateau == [["X","O",3],[4,"X","O"],[7,"O",9]] :
			choix = 9
		if plateau == [["X","O",3],[4,"X","O"],[7,8,"O"]] :
			choix = 3
		if plateau == [["X","O","X"],[4,"X","O"],["O",8,"O"]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"X","O"],[7,"O","O"]] :
			choix = 7
		if plateau == [[1,"O",3],[4,"X",6],["O",8,9]] :
			choix = 6
		if plateau == [["O","O",3],[4,"X","X"],["O",8,9]] :
			choix = 4
		if plateau == [[1,"O","O"],[4,"X","X"],["O",8,9]] :
			choix = 4
		if plateau == [[1,"O",3],["O","X","X"],["O",8,9]] :
			choix = 1
		if plateau == [["X","O","O"],["O","X","X"],["O",8,9]] :
			choix = 9
		if plateau == [["X","O",3],["O","X","X"],["O","O",9]] :
			choix = 9
		if plateau == [["X","O",3],["O","X","X"],["O",8,"O"]] :
			choix = 8
		if plateau == [[1,"O",3],[4,"X","X"],["O","O",9]] :
			choix = 4
		if plateau == [[1,"O",3],[4,"X","X"],["O",8,"O"]] :
			choix = 4
		if plateau == [[1,"O",3],[4,"X",6],[7,"O",9]] :
			choix = 1
		if plateau == [["X","O",3],[4,"X",6],["O","O",9]] :
			choix = 9
		if plateau == [["X","O",3],[4,"X",6],[7,"O","O"]] :
			choix = 7
		if plateau == [["X","O","O"],[4,"X",6],["X","O","O"]] :
			choix = 4
		if plateau == [["X","O",3],["O","X",6],["X","O","O"]] :
			choix = 3
		if plateau == [["X","O",3],[4,"X","O"],["X","O","O"]] :
			choix = 4		
		if plateau == [[1,"O",3],[4,"X",6],[7,8,"O"]] :
			choix = 4
		if plateau == [["O","O",3],["X","X",6],[7,8,"O"]] :
			choix = 6
		if plateau == [[1,"O","O"],["X","X",6],[7,8,"O"]] :
			choix = 6
		if plateau == [[1,"O",3],["X","X","O"],[7,8,"O"]] :
			choix = 3
		if plateau == [["O","O","X"],["X","X","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [[1,"O","X"],["X","X","O"],["O",8,"O"]] :
			choix = 8
		if plateau == [[1,"O","X"],["X","X","O"],[7,"O","O"]] :
			choix = 7
		if plateau == [[1,"O",3],["X","X",6],["O",8,"O"]] :
			choix = 6
		if plateau == [[1,"O",3],["X","X",6],[7,"O","O"]] :
			choix = 6			
		if plateau == [[1,2,"O"],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,"O"],["O","X",6],[7,8,9]] :
			choix = 8
		if plateau == [["O",2,"O"],["O","X",6],[7,"X",9]] :
			choix = 2
		if plateau == [[1,"O","O"],["O","X",6],[7,"X",9]] :
			choix = 1
		if plateau == [["X","O","O"],["O","X","O"],[7,"X",9]] :
			choix = 9
		if plateau == [["X","O","O"],["O","X",6],["O","X",9]] :
			choix = 9
		if plateau == [["X","O","O"],["O","X",6],[7,"X","O"]] :
			choix = 6
		if plateau == [[1,2,"O"],["O","X","O"],[7,"X",9]] :
			choix = 2
		if plateau == [[1,2,"O"],["O","X",6],["O","X",9]] :
			choix = 2
		if plateau == [[1,2,"O"],["O","X",6],[7,"X","O"]] :
			choix = 2
		if plateau == [[1,2,"O"],[4,"X","O"],[7,8,9]] :
			choix = 9
		if plateau == [["O",2,"O"],[4,"X","O"],[7,8,"X"]] :
			choix = 2
		if plateau == [["O","X","O"],["O","X","O"],[7,8,"X"]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"X","O"],["O",8,"X"]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"X","O"],[7,"O","X"]] :
			choix = 7
		if plateau == [[1,"O","O"],[4,"X","O"],[7,8,"X"]] :
			choix = 1
		if plateau == [[1,2,"O"],["O","X","O"],[7,8,"X"]] :
			choix = 1
		if plateau == [[1,2,"O"],[4,"X","O"],["O",8,"X"]] :
			choix = 1
		if plateau == [[1,2,"O"],[4,"X","O"],[7,"O","X"]] :
			choix = 1
		if plateau == [[1,2,"O"],[4,"X",6],["O",8,9]] :
			choix = 2
		if plateau == [[1,"X","O"],["O","X",6],["O",8,9]] :
			choix = 8
		if plateau == [[1,"X","O"],[4,"X","O"],["O",8,9]] :
			choix = 8
		if plateau == [[1,"X","O"],[4,"X",6],["O","O",9]] :
			choix = 9
		if plateau == [["O","X","O"],[4,"X",6],["O","O","X"]] :
			choix = 4
		if plateau == [[1,"X","O"],["O","X",6],["O","O","X"]] :
			choix = 1
		if plateau == [[1,"X","O"],[4,"X","O"],["O","O","X"]] :
			choix = 1
		if plateau == [[1,"X","O"],[4,"X",6],["O",8,"O"]] :
			choix = 8		
		if plateau == [[1,2,"O"],[4,"X",6],[7,"O",9]] :
			choix = 4
		if plateau == [["O",2,"O"],["X","X",6],[7,"O",9]] :
			choix = 6
		if plateau == [[1,"O","O"],["X","X",6],[7,"O",9]] :
			choix = 6
		if plateau == [[1,2,"O"],["X","X","O"],[7,"O",9]] :
			choix = 9
		if plateau == [["O",2,"O"],["X","X","O"],[7,"O","X"]] :
			choix = 2
		if plateau == [[1,"O","O"],["X","X","O"],[7,"O","X"]] :
			choix = 1
		if plateau == [[1,2,"O"],["X","X","O"],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,"O"],["X","X",6],["O","O",9]] :
			choix = 6
		if plateau == [[1,2,"O"],["X","X",6],[7,"O","O"]] :
			choix = 6
		if plateau == [[1,2,"O"],[4,"X",6],[7,8,"O"]] :
			choix = 6
		if plateau == [["O",2,"O"],[4,"X","X"],[7,8,"O"]] :
			choix = 4 
		if plateau == [[1,"O","O"],[4,"X","X"],[7,8,"O"]] :
			choix = 4
		if plateau == [[1,2,"O"],["O","X","X"],[7,8,"O"]] :
			choix = 2
		if plateau == [["O","X","O"],["O","X","X"],[7,8,"O"]] :
			choix = 8
		if plateau == [[1,"X","O"],["O","X","X"],["O",8,"O"]] :
			choix = 8
		if plateau == [[1,"X","O"],["O","X","X"],[7,"O","O"]] :
			choix = 7
		if plateau == [[1,2,"O"],[4,"X","X"],["O",8,"O"]] :
			choix = 4
		if plateau == [[1,2,"O"],[4,"X","X"],[7,"O","O"]] :
			choix = 4
		if plateau == [[1,2,3],["O",5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,3],["O","X","O"],[7,8,9]] :
			choix = 1
		if plateau == [["X",2,"O"],["O","X","O"],[7,8,9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X","O"],["O",8,9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X","O"],[7,"O",9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X","O"],[7,8,"O"]] :
			choix = 3
		if plateau == [["X",2,"X"],["O","X","O"],["O",8,"O"]] :
			choix = 2
		if plateau == [["X",2,"X"],["O","X","O"],[7,"O","O"]] :
			choix = 2
		if plateau == [[1,2,3],["O","X",6],["O",8,9]] :
			choix = 1
		if plateau == [["X",2,"O"],["O","X",6],["O",8,9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X",6],["O","O",9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["X","O",3],["O","X",6],["O","X","O"]] :
			choix = 3
		if plateau == [["X",2,"O"],["O","X",6],["O","X","O"]] :
			choix = 2
		if plateau == [["X",2,3],["O","X","O"],["O","X","O"]] :
			choix = 2	
		if plateau == [[1,2,3],["O","X",6],[7,"O",9]] :
			choix = 1
		if plateau == [["X",2,"O"],["O","X",6],[7,"O",9]] :
			choix = 9
		if plateau == [["X",2,3],["O","X",6],[7,"O","O"]] :
			choix = 7
		if plateau == [["X",2,"O"],["O","X",6],["X","O","O"]] :
			choix = 6
		if plateau == [["X",2,3],["O","X","O"],["X","O","O"]] :
			choix = 3	
		if plateau == [[1,2,3],["O","X",6],[7,8,"O"]] :
			choix = 2
		if plateau == [[1,"X","O"],["O","X",6],[7,8,"O"]] :
			choix = 8
		if plateau == [[1,"X",3],["O","X","O"],[7,8,"O"]] :
			choix = 8
		if plateau == [[1,"X",3],["O","X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [[1,"X",3],["O","X",6],[7,"O","O"]] :
			choix = 7
		if plateau == [[1,"X","O"],["O","X",6],["X","O","O"]] :
			choix = 6
		if plateau == [[1,"X",3],["O","X","O"],["X","O","O"]] :
			choix = 3			
		if plateau == [[1,2,3],[4,"O",6],[7,8,9]] :
			choix = 1
		if plateau == [["X","O",3],[4,"O",6],[7,8,9]] :
			choix = 8
		if plateau == [["X","O","O"],[4,"O",6],[7,"X",9]] :
			choix = 7
		if plateau == [["X","O","O"],["O","O",6],["X","X",9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"O","O"],["X","X",9]] :
			choix = 9
		if plateau == [["X","O","O"],[4,"O",6],["X","X","O"]] :
			choix = 4
		if plateau == [["X","O",3],["O","O",6],[7,"X",9]] :
			choix = 6
		if plateau == [["X","O","O"],["O","O","X"],[7,"X",9]] :
			choix = 7
		if plateau == [["X","O",3],["O","O","X"],["O","X",9]] :
			choix = 3
		if plateau == [["X","O",3],["O","O","X"],[7,"X","O"]] :
			choix = 3
		if plateau == [["X","O",3],[4,"O","O"],[7,"X",9]] :
			choix = 4
		if plateau == [["X","O","O"],["X","O","O"],[7,"X",9]] :
			choix = 7
		if plateau == [["X","O",3],["X","O","O"],["O","X",9]] :
			choix = 3
		if plateau == [["X","O",3],["X","O","O"],[7,"X","O"]] :
			choix = 7
		if plateau == [["X","O",3],[4,"O",6],["O","X",9]] :
			choix = 3
		if plateau == [["X","O","X"],["O","O",6],["O","X",9]] :
			choix = 6
		if plateau == [["X","O","X"],[4,"O","O"],["O","X",9]] :
			choix = 4
		if plateau == [["X","O","X"],[4,"O",6],["O","X","O"]] :
			choix = 4	
		if plateau == [["X","O",3],[4,"O",6],[7,"X","O"]] :
			choix = 7
		if plateau == [["X","O",3],["O","O",6],["X","X","O"]] :
			choix = 6
		if plateau == [["X","O",3],[4,"O","O"],["X","X","O"]] :
			choix = 4		
		if plateau == [["X",2,"O"],[4,"O",6],[7,8,9]] :
			choix = 7
		if plateau == [["X","O","O"],[4,"O",6],["X",8,9]] :
			choix = 4
		if plateau == [["X",2,"O"],["O","O",6],["X",8,9]] :
			choix = 6
		if plateau == [["X","O","O"],["O","O","X"],["X",8,9]] :
			choix = 8
		if plateau == [["X",2,"O"],["O","O","X"],["X","O",9]] :
			choix = 2
		if plateau == [["X",2,"O"],["O","O","X"],["X",8,"O"]] :
			choix = 8
		if plateau == [["X",2,"O"],[4,"O","O"],["X",8,9]] :
			choix = 4
		if plateau == [["X",2,"O"],[4,"O",6],["X","O",9]] :
			choix = 4
		if plateau == [["X",2,"O"],[4,"O",6],["X",8,"O"]] :
			choix = 4	
		if plateau == [["X",2,3],["O","O",6],[7,8,9]] :
			choix = 6
		if plateau == [["X","O",3],["O","O","X"],[7,8,9]] :
			choix = 8	
		if plateau == [["X",2,"O"],["O","O","X"],[7,8,9]] :
			choix = 7
		if plateau == [["X",2,3],["O","O","X"],["O",8,9]] :
			choix = 3
		if plateau == [["X","O","X"],["O","O","X"],["O",8,9]] :
			choix = 9
		if plateau == [["X",2,"X"],["O","O","X"],["O","O",9]] :
			choix = 9
		if plateau == [["X",2,"X"],["O","O","X"],["O",8,"O"]] :
			choix = 2	
		if plateau == [["X",2,3],["O","O","X"],[7,"O",9]] :
			choix = 2
		if plateau == [["X","X","O"],["O","O","X"],[7,"O",9]] :
			choix = 7
		if plateau == [["X","X",3],["O","O","X"],["O","O",9]] :
			choix = 3
		if plateau == [["X","X",3],["O","O","X"],[7,"O","O"]] :
			choix = 3	
		if plateau == [["X",2,3],["O","O","X"],[7,8,"O"]] :
			choix = 2
		if plateau == [["X","X","O"],["O","O","X"],[7,8,"O"]] :
			choix = 7
		if plateau == [["X","X",3],["O","O","X"],["O",8,"O"]] :
			choix = 3	
		if plateau == [["X",2,3],[4,"O","O"],[7,8,9]] :
			choix = 4
		if plateau == [["X","O",3],["X","O","O"],[7,8,9]] :
			choix = 7
		if plateau == [["X",2,"O"],["X","O","O"],[7,8,9]] :
			choix = 7
		if plateau == [["X",2,3],["X","O","O"],["O",8,9]] :
			choix = 3
		if plateau == [["X","O","X"],["X","O","O"],["O",8,9]] :
			choix = 8
		if plateau == [["X",2,"X"],["X","O","O"],["O","O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],["X","O","O"],["O",8,"O"]] :
			choix = 2
		if plateau == [["X",2,3],["X","O","O"],[7,"O",9]] :
			choix = 7
		if plateau == [["X",2,3],["X","O","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [["X",2,3],[4,"O",6],["O",8,9]] :
			choix = 3
		if plateau == [["X","O","X"],[4,"O",6],["O",8,9]] :
			choix = 8	
		if plateau == [["X",2,"X"],["O","O",6],["O",8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O","O"],["O",8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],["O","O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],["O",8,"O"]] :
			choix = 2				
		if plateau == [["X",2,3],[4,"O",6],[7,"O",9]] :
			choix = 2
		if plateau == [["X","X","O"],[4,"O",6],[7,"O",9]] :
			choix = 7
		if plateau == [["X","X","O"],["O","O",6],["X","O",9]] :
			choix = 6
		if plateau == [["X","X","O"],[4,"O","O"],["X","O",9]] :
			choix = 4
		if plateau == [["X","X","O"],[4,"O",6],["X","O","O"]] :
			choix = 4
		if plateau == [["X","X",3],["O","O",6],[7,"O",9]] :
			choix = 3
		if plateau == [["X","X",3],[4,"O","O"],[7,"O",9]] :
			choix = 3
		if plateau == [["X","X",3],[4,"O",6],["O","O",9]] :
			choix = 3
		if plateau == [["X","X",3],[4,"O",6],[7,"O","O"]] :
			choix = 3	
		if plateau == [["X",2,3],[4,"O",6],[7,8,"O"]] :
			choix = 3
		if plateau == [["X","O","X"],[4,"O",6],[7,8,"O"]] :
			choix = 8
		if plateau == [["X","O","X"],["O","O",6],[7,"X","O"]] :
			choix = 6
		if plateau == [["X","O","X"],[4,"O","O"],[7,"X","O"]] :
			choix = 4
		if plateau == [["X",2,"X"],["O","O",6],[7,8,"O"]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O","O"],[7,8,"O"]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],[7,"O","O"]] :
			choix = 2	
		if plateau == [[1,2,3],[4,5,"O"],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"X","O"],["O",8,9]] :
			choix = 2
		if plateau == [[1,"X",3],["O","X","O"],["O",8,9]] :
			choix = 8
		if plateau == [[1,"X",3],[4,"X","O"],["O","O",9]] :
			choix = 9
		if plateau == [["O","X",3],[4,"X","O"],["O","O","X"]] :
			choix = 4
		if plateau == [[1,"X",3],["O","X","O"],["O","O","X"]] :
			choix = 1
		if plateau == [[1,"X",3],[4,"X","O"],["O",8,"O"]] :
			choix = 8		
		if plateau == [[1,2,3],[4,"X","O"],[7,"O",9]] :
			choix = 3
		if plateau == [["O",2,"X"],[4,"X","O"],[7,"O",9]] :
			choix = 7
		if plateau == [[1,"O","X"],[4,"X","O"],[7,"O",9]] :
			choix = 7
		if plateau == [[1,2,"X"],["O","X","O"],[7,"O",9]] :
			choix = 7
		if plateau == [[1,2,"X"],[4,"X","O"],["O","O",9]] :
			choix = 9
		if plateau == [["O",2,"X"],[4,"X","O"],["O","O","X"]] :
			choix = 4
		if plateau == [[1,"O","X"],[4,"X","O"],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,"X"],["O","X","O"],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,"X"],[4,"X","O"],[7,"O","O"]] :
			choix = 7	
		if plateau == [[1,2,3],[4,"X","O"],[7,8,"O"]] :
			choix = 3
		if plateau == [["O",2,"X"],[4,"X","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [[1,"O","X"],[4,"X","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [[1,2,"X"],["O","X","O"],[7,8,"O"]] :
			choix = 7
		if plateau == [[1,2,"X"],[4,"X","O"],["O",8,"O"]] :
			choix = 8
		if plateau == [["O",2,"X"],[4,"X","O"],["O","X","O"]] :
			choix = 2
		if plateau == [[1,"O","X"],[4,"X","O"],["O","X","O"]] :
			choix = 1
		if plateau == [[1,2,"X"],["O","X","O"],["O","X","O"]] :
			choix = 2	
		if plateau == [[1,2,3],[4,5,6],["O",8,9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"X",6],["O","O",9]] :
			choix = 9
		if plateau == [["O",2,3],[4,"X",6],["O","O","X"]] :
			choix = 4
		if plateau == [["O","O",3],["X","X",6],["O","O","X"]] :
			choix = 6
		if plateau == [["O",2,"O"],["X","X",6],["O","O","X"]] :
			choix = 6
		if plateau == [["O",2,3],["X","X","O"],["O","O","X"]] :
			choix = 3
		if plateau == [[1,"O",3],[4,"X",6],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,"O"],[4,"X",6],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,3],["O","X",6],["O","O","X"]] :
			choix = 1
		if plateau == [[1,2,3],[4,"X","O"],["O","O","X"]] :
			choix = 1	
		if plateau == [[1,2,3],[4,"X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["O",2,3],[4,"X",6],["O","X","O"]] :
			choix = 2
		if plateau == [[1,"O",3],[4,"X",6],["O","X","O"]] :
			choix = 4
		if plateau == [["O","O",3],["X","X",6],["O","X","O"]] :
			choix = 6
		if plateau == [[1,"O","O"],["X","X",6],["O","X","O"]] :
			choix = 6
		if plateau == [[1,"O",3],["X","X","O"],["O","X","O"]] :
			choix = 3
		if plateau == [[1,2,"O"],[4,"X",6],["O","X","O"]] :
			choix = 2
		if plateau == [[1,2,3],["O","X",6],["O","X","O"]] :
			choix = 2
		if plateau == [[1,2,3],[4,"X","O"],["O","X","O"]] :
			choix = 2
		if plateau == [[1,2,3],[4,5,6],[7,"O",9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"X",6],[7,"O","O"]] :
			choix = 7
		if plateau == [["O",2,3],[4,"X",6],["X","O","O"]] :
			choix = 3
		if plateau == [[1,"O",3],[4,"X",6],["X","O","O"]] :
			choix = 3
		if plateau == [[1,2,"O"],[4,"X",6],["X","O","O"]] :
			choix = 6
		if plateau == [["O",2,"O"],[4,"X","X"],["X","O","O"]] :
			choix = 4
		if plateau == [[1,"O","O"],[4,"X","X"],["X","O","O"]] :
			choix = 4
		if plateau == [[1,2,"O"],["O","X","X"],["X","O","O"]] :
			choix = 1
		if plateau == [[1,2,3],["O","X",6],["X","O","O"]] :
			choix = 3
		if plateau == [[1,2,3],[4,"X","O"],["X","O","O"]] :
			choix = 3	
		if plateau == [[1,2,3],[4,5,6],[7,8,"O"]] :
			choix = 5
	if premier_joueur == "joueur" and symbole == "X" :
		if plateau == [["X",2,3],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [["X","X",3],[4,"O",6],[7,8,9]] :
			choix = 3
		if plateau == [["X","X","O"],["X","O",6],[7,8,9]] :
			choix = 7
		if plateau == [["X","X","O"],[4,"O","X"],[7,8,9]] :
			choix = 7
		if plateau == [["X","X","O"],[4,"O",6],["X",8,9]] :
			choix = 4
		if plateau == [["X","X","O"],["O","O","X"],["X",8,9]] :
			choix = 9
		if plateau == [["X","X","O"],["O","O",6],["X","X",9]] :
			choix = 6
		if plateau == [["X","X","O"],["O","O",6],["X",8,"X"]] :
			choix = 6
		if plateau == [["X","X","O"],["X","O","X"],["X",8,9]] :
			choix = 9
		if plateau == [["X","X","O"],[4,"O",6],[7,"X",9]] :
			choix = 7
		if plateau == [["X","X","O"],[4,"O",6],[7,8,"X"]] :
			choix = 7	
		if plateau == [["X",2,"X"],[4,"O",6],[7,8,9]] :
			choix = 2
		if plateau == [["X","O","X"],["X","O",6],[7,8,9]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"O","X"],[7,8,9]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"O",6],["X",8,9]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"O",6],[7,"X",9]] :
			choix = 4
		if plateau == [["X","O","X"],["O","O","X"],[7,"X",9]] :
			choix = 9 
		if plateau == [["X","O","X"],["O","O",6],["X","X",9]] :
			choix = 6
		if plateau == [["X","O","X"],["O","O",6],[7,"X","X"]] :
			choix = 6
		if plateau == [["X","O","X"],["O","O",6],[7,8,"X"]] :
			choix = 8	
		if plateau == [["X",2,3],["X","O",6],[7,8,9]] :
			choix = 7
		if plateau == [["X","X",3],["X","O",6],["O",8,9]] :
			choix = 3
		if plateau == [["X",2,"X"],["X","O",6],["O",8,9]] :
			choix = 2
		if plateau == [["X","O","X"],["X","O","X"],["O",8,9]] :
			choix = 8
		if plateau == [["X","O","X"],["X","O",6],["O","X",9]] :
			choix = 9
		if plateau == [["X","O","X"],["X","O",6],["O",8,"X"]] :
			choix = 8
		if plateau == [["X",2,3],["X","O","X"],["O",8,9]] :
			choix = 3
		if plateau == [["X",2,3],["X","O",6],["O","X",9]] :
			choix = 3
		if plateau == [["X",2,3],["X","O",6],["O",8,"X"]] :
			choix = 3
		if plateau == [["X",2,3],[4,"O","X"],[7,8,9]] :
			choix = 2
		if plateau == [["X","O",3],["X","O","X"],[7,8,9]] :
			choix = 8
		if plateau == [["X","O",3],[4,"O","X"],["X",8,9]] :
			choix = 8
		if plateau == [["X","O",3],[4,"O","X"],[7,"X",9]] :
			choix = 7
		if plateau == [["X","O","X"],[4,"O","X"],["O","X",9]] :
			choix = 9
		if plateau == [["X","O",3],["X","O","X"],["O","X",9]] :
			choix = 3
		if plateau == [["X","O",3],[4,"O","X"],["O","X","X"]] :
			choix = 3
		if plateau == [["X","O",3],[4,"O","X"],[7,8,"X"]] :
			choix = 8
		if plateau == [["X",2,3],[4,"O",6],["X",8,9]] :
			choix = 4
		if plateau == [["X","X",3],["O","O",6],["X",8,9]] :
			choix = 6
		if plateau == [["X",2,"X"],["O","O",6],["X",8,9]] :
			choix = 6
		if plateau == [["X",2,3],["O","O","X"],["X",8,9]] :
			choix = 2
		if plateau == [["X","O","X"],["O","O","X"],["X",8,9]] :
			choix = 8
		if plateau == [["X","O",3],["O","O","X"],["X","X",9]] :
			choix = 9
		if plateau == [["X","O",3],["O","O","X"],["X",8,"X"]] :
			choix = 8
		if plateau == [["X",2,3],["O","O",6],["X","X",9]] :
			choix = 6
		if plateau == [["X",2,3],["O","O",6],["X",8,"X"]] :
			choix = 6
		if plateau == [["X",2,3],[4,"O",6],[7,"X",9]] :
			choix = 6
		if plateau == [["X","X",3],[4,"O","O"],[7,"X",9]] :
			choix = 4
		if plateau == [["X",2,"X"],[4,"O","O"],[7,"X",9]] :
			choix = 4
		if plateau == [["X",2,3],["X","O","O"],[7,"X",9]] :
			choix = 7
		if plateau == [["X","X",3],["X","O","O"],["O","X",9]] :
			choix = 3
		if plateau == [["X",2,"X"],["X","O","O"],["O","X",9]] :
			choix = 2
		if plateau == [["X",2,3],["X","O","O"],["O","X","X"]] :
			choix = 3
		if plateau == [["X",2,3],[4,"O","O"],["X","X",9]] :
			choix = 4
		if plateau == [["X",2,3],[4,"O","O"],[7,"X","X"]] :
			choix = 4	
		if plateau == [["X",2,3],[4,"O",6],[7,8,"X"]] :
			choix = 2
		if plateau == [["X","O","X"],[4,"O",6],[7,8,"X"]] :
			choix = 8
		if plateau == [["X","O",3],["X","O",6],[7,8,"X"]] :
			choix = 8
		if plateau == [["X","O",3],[4,"O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["X","O",3],[4,"O",6],[7,"X","X"]] :
			choix = 7
		if plateau == [["X","O","X"],[4,"O",6],["O","X","X"]] :
			choix = 6
		if plateau == [["X","O",3],["X","O",6],["O","X","X"]] :
			choix = 3
		if plateau == [[1,"X",3],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,"X","X"],[4,"O",6],[7,8,9]] :
			choix = 1
		if plateau == [["O","X","X"],["X","O",6],[7,8,9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"O","X"],[7,8,9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"O",6],["X",8,9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"O",6],[7,"X",9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"O",6],[7,8,"X"]] :
			choix = 6
		if plateau == [["O","X","X"],["X","O","O"],[7,8,"X"]] :
			choix = 7
		if plateau == [["O","X","X"],[4,"O","O"],["X",8,"X"]] :
			choix = 4
		if plateau == [["O","X","X"],[4,"O","O"],[7,"X","X"]] :
			choix = 4
		if plateau == [[1,"X",3],["X","O",6],[7,8,9]] :
			choix = 1
		if plateau == [["O","X",3],["X","O","X"],[7,8,9]] :
			choix = 9
		if plateau == [["O","X",3],["X","O",6],["X",8,9]] :
			choix = 9
		if plateau == [["O","X",3],["X","O",6],[7,"X",9]] :
			choix = 9
		if plateau == [["O","X",3],["X","O",6],[7,8,"X"]] :
			choix = 3
		if plateau == [["O","X","O"],["X","O","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [["O","X","O"],["X","O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["O","X","O"],["X","O",6],["X",8,"X"]] :
			choix = 6
		if plateau == [["O","X","O"],["X","O",6],[7,"X","X"]] :
			choix = 7		
		if plateau == [[1,"X",3],[4,"O","X"],[7,8,9]] :
			choix = 1
		if plateau == [["O","X",3],[4,"O","X"],["X",8,9]] :
			choix = 9
		if plateau == [["O","X",3],[4,"O","X"],[7,"X",9]] :
			choix = 9
		if plateau == [["O","X",3],[4,"O","X"],[7,8,"X"]] :
			choix = 3
		if plateau == [["O","X","O"],[4,"O","X"],["X",8,"X"]] :
			choix = 8
		if plateau == [["O","X","O"],[4,"O","X"],[7,"X","X"]] :
			choix = 7
		if plateau == [[1,"X",3],[4,"O",6],["X",8,9]] :
			choix = 6
		if plateau == [["X","X",3],[4,"O","O"],["X",8,9]] :
			choix = 4
		if plateau == [[1,"X","X"],[4,"O","O"],["X",8,9]] :
			choix = 4
		if plateau == [[1,"X",3],["X","O","O"],["X",8,9]] :
			choix = 1
		if plateau == [["O","X","X"],["X","O","O"],["X",8,9]] :
			choix = 9
		if plateau == [["O","X",3],["X","O","O"],["X","X",9]] :
			choix = 9
		if plateau == [["O","X",3],["X","O","O"],["X",8,"X"]] :
			choix = 8
		if plateau == [[1,"X",3],[4,"O","O"],["X","X",9]] :
			choix = 4
		if plateau == [[1,"X",3],[4,"O","O"],["X",8,"X"]] :
			choix = 4
		if plateau == [[1,"X",3],[4,"O",6],[7,"X",9]] :
			choix = 1
		if plateau == [["O","X",3],[4,"O",6],["X","X",9]] :
			choix = 9
		if plateau == [["O","X",3],[4,"O",6],[7,"X","X"]] :
			choix = 7
		if plateau == [["O","X","X"],[4,"O",6],["O","X","X"]] :
			choix = 4
		if plateau == [["O","X",3],["X","O",6],["O","X","X"]] :
			choix = 3
		if plateau == [["O","X",3],[4,"O","X"],["O","X","X"]] :
			choix = 4		
		if plateau == [[1,"X",3],[4,"O",6],[7,8,"X"]] :
			choix = 4
		if plateau == [["X","X",3],["O","O",6],[7,8,"X"]] :
			choix = 6
		if plateau == [[1,"X","X"],["O","O",6],[7,8,"X"]] :
			choix = 6
		if plateau == [[1,"X",3],["O","O","X"],[7,8,"X"]] :
			choix = 3
		if plateau == [["X","X","O"],["O","O","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [[1,"X","O"],["O","O","X"],["X",8,"X"]] :
			choix = 8
		if plateau == [[1,"X","O"],["O","O","X"],[7,"X","X"]] :
			choix = 7
		if plateau == [[1,"X",3],["O","O",6],["X",8,"X"]] :
			choix = 6
		if plateau == [[1,"X",3],["O","O",6],[7,"X","X"]] :
			choix = 6			
		if plateau == [[1,2,"X"],[4,5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,"X"],["X","O",6],[7,8,9]] :
			choix = 8
		if plateau == [["X",2,"X"],["X","O",6],[7,"O",9]] :
			choix = 2
		if plateau == [[1,"X","X"],["X","O",6],[7,"O",9]] :
			choix = 1
		if plateau == [["O","X","X"],["X","O","X"],[7,"O",9]] :
			choix = 9
		if plateau == [["O","X","X"],["X","O",6],["X","O",9]] :
			choix = 9
		if plateau == [["O","X","X"],["X","O",6],[7,"O","X"]] :
			choix = 6
		if plateau == [[1,2,"X"],["X","O","X"],[7,"O",9]] :
			choix = 2
		if plateau == [[1,2,"X"],["X","O",6],["X","O",9]] :
			choix = 2
		if plateau == [[1,2,"X"],["X","O",6],[7,"O","X"]] :
			choix = 2
		if plateau == [[1,2,"X"],[4,"O","X"],[7,8,9]] :
			choix = 9
		if plateau == [["X",2,"X"],[4,"O","X"],[7,8,"O"]] :
			choix = 2
		if plateau == [["X","O","X"],["X","O","X"],[7,8,"O"]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"O","X"],["X",8,"O"]] :
			choix = 8
		if plateau == [["X","O","X"],[4,"O","X"],[7,"X","O"]] :
			choix = 7
		if plateau == [[1,"X","X"],[4,"O","X"],[7,8,"O"]] :
			choix = 1
		if plateau == [[1,2,"X"],["X","O","X"],[7,8,"O"]] :
			choix = 1
		if plateau == [[1,2,"X"],[4,"O","X"],["X",8,"O"]] :
			choix = 1
		if plateau == [[1,2,"X"],[4,"O","X"],[7,"X","O"]] :
			choix = 1
		if plateau == [[1,2,"X"],[4,"O",6],["X",8,9]] :
			choix = 2
		if plateau == [[1,"O","X"],["X","O",6],["X",8,9]] :
			choix = 8
		if plateau == [[1,"O","X"],[4,"O","X"],["X",8,9]] :
			choix = 8
		if plateau == [[1,"O","X"],[4,"O",6],["X","X",9]] :
			choix = 9
		if plateau == [["X","O","X"],[4,"O",6],["X","X","O"]] :
			choix = 4
		if plateau == [[1,"O","X"],["X","O",6],["X","X","O"]] :
			choix = 1
		if plateau == [[1,"O","X"],[4,"O","X"],["X","X","O"]] :
			choix = 1
		if plateau == [[1,"O","X"],[4,"O",6],["X",8,"X"]] :
			choix = 8		
		if plateau == [[1,2,"X"],[4,"O",6],[7,"X",9]] :
			choix = 4
		if plateau == [["X",2,"X"],["O","O",6],[7,"X",9]] :
			choix = 6
		if plateau == [[1,"X","X"],["O","O",6],[7,"X",9]] :
			choix = 6
		if plateau == [[1,2,"X"],["O","O","X"],[7,"X",9]] :
			choix = 9
		if plateau == [["X",2,"X"],["O","O","X"],[7,"X","O"]] :
			choix = 2
		if plateau == [[1,"X","X"],["O","O","X"],[7,"X","O"]] :
			choix = 1
		if plateau == [[1,2,"X"],["O","O","X"],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,"X"],["O","O",6],["X","X",9]] :
			choix = 6
		if plateau == [[1,2,"X"],["O","O",6],[7,"X","X"]] :
			choix = 6
		if plateau == [[1,2,"X"],[4,"O",6],[7,8,"X"]] :
			choix = 6
		if plateau == [["X",2,"X"],[4,"O","O"],[7,8,"X"]] :
			choix = 4 
		if plateau == [[1,"X","X"],[4,"O","O"],[7,8,"X"]] :
			choix = 4
		if plateau == [[1,2,"X"],["X","O","O"],[7,8,"X"]] :
			choix = 2
		if plateau == [["X","O","X"],["X","O","O"],[7,8,"X"]] :
			choix = 8
		if plateau == [[1,"O","X"],["X","O","O"],["X",8,"X"]] :
			choix = 8
		if plateau == [[1,"O","X"],["X","O","O"],[7,"X","X"]] :
			choix = 7
		if plateau == [[1,2,"X"],[4,"O","O"],["X",8,"X"]] :
			choix = 4
		if plateau == [[1,2,"X"],[4,"O","O"],[7,"X","X"]] :
			choix = 4
		if plateau == [[1,2,3],["X",5,6],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,3],["X","O","X"],[7,8,9]] :
			choix = 1
		if plateau == [["O",2,"X"],["X","O","X"],[7,8,9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O","X"],["X",8,9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O","X"],[7,"X",9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O","X"],[7,8,"X"]] :
			choix = 3
		if plateau == [["O",2,"O"],["X","O","X"],["X",8,"X"]] :
			choix = 2
		if plateau == [["O",2,"O"],["X","O","X"],[7,"X","X"]] :
			choix = 2
		if plateau == [[1,2,3],["X","O",6],["X",8,9]] :
			choix = 1
		if plateau == [["O",2,"X"],["X","O",6],["X",8,9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O",6],["X","X",9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["O","X",3],["X","O",6],["X","O","X"]] :
			choix = 3
		if plateau == [["O",2,"X"],["X","O",6],["X","O","X"]] :
			choix = 2
		if plateau == [["O",2,3],["X","O","X"],["X","O","X"]] :
			choix = 2	
		if plateau == [[1,2,3],["X","O",6],[7,"X",9]] :
			choix = 1
		if plateau == [["O",2,"X"],["X","O",6],[7,"X",9]] :
			choix = 9
		if plateau == [["O",2,3],["X","O",6],[7,"X","X"]] :
			choix = 7
		if plateau == [["O",2,"X"],["X","O",6],["O","X","X"]] :
			choix = 6
		if plateau == [["O",2,3],["X","O","X"],["O","X","X"]] :
			choix = 3	
		if plateau == [[1,2,3],["X","O",6],[7,8,"X"]] :
			choix = 2
		if plateau == [[1,"O","X"],["X","O",6],[7,8,"X"]] :
			choix = 8
		if plateau == [[1,"O",3],["X","O","X"],[7,8,"X"]] :
			choix = 8
		if plateau == [[1,"O",3],["X","O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [[1,"O",3],["X","O",6],[7,"X","X"]] :
			choix = 7
		if plateau == [[1,"O","X"],["X","O",6],["O","X","X"]] :
			choix = 6
		if plateau == [[1,"O",3],["X","O","X"],["O","X","X"]] :
			choix = 3			
		if plateau == [[1,2,3],[4,"X",6],[7,8,9]] :
			choix = 1
		if plateau == [["O","X",3],[4,"X",6],[7,8,9]] :
			choix = 8
		if plateau == [["O","X","X"],[4,"X",6],[7,"O",9]] :
			choix = 7
		if plateau == [["O","X","X"],["X","X",6],["O","O",9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"X","X"],["O","O",9]] :
			choix = 9
		if plateau == [["O","X","X"],[4,"X",6],["O","O","X"]] :
			choix = 4
		if plateau == [["O","X",3],["X","X",6],[7,"O",9]] :
			choix = 6
		if plateau == [["O","X","X"],["X","X","O"],[7,"O",9]] :
			choix = 7
		if plateau == [["O","X",3],["X","X","O"],["X","O",9]] :
			choix = 3
		if plateau == [["O","X",3],["X","X","O"],[7,"O","X"]] :
			choix = 3
		if plateau == [["O","X",3],[4,"X","X"],[7,"O",9]] :
			choix = 4
		if plateau == [["O","X","X"],["O","X","X"],[7,"O",9]] :
			choix = 7
		if plateau == [["O","X",3],["O","X","X"],["X","O",9]] :
			choix = 3
		if plateau == [["O","X",3],["O","X","X"],[7,"O","X"]] :
			choix = 7
		if plateau == [["O","X",3],[4,"X",6],["X","O",9]] :
			choix = 3
		if plateau == [["O","X","O"],["X","X",6],["X","O",9]] :
			choix = 6
		if plateau == [["O","X","O"],[4,"X","X"],["X","O",9]] :
			choix = 4
		if plateau == [["O","X","O"],[4,"X",6],["X","O","X"]] :
			choix = 4	
		if plateau == [["O","X",3],[4,"X",6],[7,"O","X"]] :
			choix = 7
		if plateau == [["O","X",3],["X","X",6],["O","O","X"]] :
			choix = 6
		if plateau == [["O","X",3],[4,"X","X"],["O","O","X"]] :
			choix = 4		
		if plateau == [["O",2,"X"],[4,"X",6],[7,8,9]] :
			choix = 7
		if plateau == [["O","X","X"],[4,"X",6],["O",8,9]] :
			choix = 4
		if plateau == [["O",2,"X"],["X","X",6],["O",8,9]] :
			choix = 6
		if plateau == [["O","X","X"],["X","X","O"],["O",8,9]] :
			choix = 8
		if plateau == [["O",2,"X"],["X","X","O"],["O","X",9]] :
			choix = 2
		if plateau == [["O",2,"X"],["X","X","O"],["O",8,"X"]] :
			choix = 8
		if plateau == [["O",2,"X"],[4,"X","X"],["O",8,9]] :
			choix = 4
		if plateau == [["O",2,"X"],[4,"X",6],["O","X",9]] :
			choix = 4
		if plateau == [["O",2,"X"],[4,"X",6],["O",8,"X"]] :
			choix = 4	
		if plateau == [["O",2,3],["X","X",6],[7,8,9]] :
			choix = 6
		if plateau == [["O","X",3],["X","X","O"],[7,8,9]] :
			choix = 8	
		if plateau == [["O",2,"X"],["X","X","O"],[7,8,9]] :
			choix = 7
		if plateau == [["O",2,3],["X","X","O"],["X",8,9]] :
			choix = 3
		if plateau == [["O","X","O"],["X","X","O"],["X",8,9]] :
			choix = 9
		if plateau == [["O",2,"O"],["X","X","O"],["X","X",9]] :
			choix = 9
		if plateau == [["O",2,"O"],["X","X","O"],["X",8,"X"]] :
			choix = 2	
		if plateau == [["O",2,3],["X","X","O"],[7,"X",9]] :
			choix = 2
		if plateau == [["O","O","X"],["X","X","O"],[7,"X",9]] :
			choix = 7
		if plateau == [["O","O",3],["X","X","O"],["X","X",9]] :
			choix = 3
		if plateau == [["O","O",3],["X","X","O"],[7,"X","X"]] :
			choix = 3	
		if plateau == [["O",2,3],["X","X","O"],[7,8,"X"]] :
			choix = 2
		if plateau == [["O","O","X"],["X","X","O"],[7,8,"X"]] :
			choix = 7
		if plateau == [["O","O",3],["X","X","O"],["X",8,"X"]] :
			choix = 3	
		if plateau == [["O",2,3],[4,"X","X"],[7,8,9]] :
			choix = 4
		if plateau == [["O","X",3],["O","X","X"],[7,8,9]] :
			choix = 7
		if plateau == [["O",2,"X"],["O","X","X"],[7,8,9]] :
			choix = 7
		if plateau == [["O",2,3],["O","X","X"],["X",8,9]] :
			choix = 3
		if plateau == [["O","X","O"],["O","X","X"],["X",8,9]] :
			choix = 8
		if plateau == [["O",2,"O"],["O","X","X"],["X","X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],["O","X","X"],["X",8,"X"]] :
			choix = 2
		if plateau == [["O",2,3],["O","X","X"],[7,"X",9]] :
			choix = 7
		if plateau == [["O",2,3],["O","X","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [["O",2,3],[4,"X",6],["X",8,9]] :
			choix = 3
		if plateau == [["O","X","O"],[4,"X",6],["X",8,9]] :
			choix = 8	
		if plateau == [["O",2,"O"],["X","X",6],["X",8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],["X","X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],["X",8,"X"]] :
			choix = 2				
		if plateau == [["O",2,3],[4,"X",6],[7,"X",9]] :
			choix = 2
		if plateau == [["O","O","X"],[4,"X",6],[7,"X",9]] :
			choix = 7
		if plateau == [["O","O","X"],["X","X",6],["O","X",9]] :
			choix = 6
		if plateau == [["O","O","X"],[4,"X","X"],["O","X",9]] :
			choix = 4
		if plateau == [["O","O","X"],[4,"X",6],["O","X","X"]] :
			choix = 4
		if plateau == [["O","O",3],["X","X",6],[7,"X",9]] :
			choix = 3
		if plateau == [["O","O",3],[4,"X","X"],[7,"X",9]] :
			choix = 3
		if plateau == [["O","O",3],[4,"X",6],["X","X",9]] :
			choix = 3
		if plateau == [["O","O",3],[4,"X",6],[7,"X","X"]] :
			choix = 3	
		if plateau == [["O",2,3],[4,"X",6],[7,8,"X"]] :
			choix = 3
		if plateau == [["O","X","O"],[4,"X",6],[7,8,"X"]] :
			choix = 8
		if plateau == [["O","X","O"],["X","X",6],[7,"O","X"]] :
			choix = 6
		if plateau == [["O","X","O"],[4,"X","X"],[7,"O","X"]] :
			choix = 4
		if plateau == [["O",2,"O"],["X","X",6],[7,8,"X"]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X","X"],[7,8,"X"]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],[7,"X","X"]] :
			choix = 2	
		if plateau == [[1,2,3],[4,5,"X"],[7,8,9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"O","X"],["X",8,9]] :
			choix = 2
		if plateau == [[1,"O",3],["X","O","X"],["X",8,9]] :
			choix = 8
		if plateau == [[1,"O",3],[4,"O","X"],["X","X",9]] :
			choix = 9
		if plateau == [["X","O",3],[4,"O","X"],["X","X","O"]] :
			choix = 4
		if plateau == [[1,"O",3],["X","O","X"],["X","X","O"]] :
			choix = 1
		if plateau == [[1,"O",3],[4,"O","X"],["X",8,"X"]] :
			choix = 8		
		if plateau == [[1,2,3],[4,"O","X"],[7,"X",9]] :
			choix = 3
		if plateau == [["X",2,"O"],[4,"O","X"],[7,"X",9]] :
			choix = 7
		if plateau == [[1,"X","O"],[4,"O","X"],[7,"X",9]] :
			choix = 7
		if plateau == [[1,2,"O"],["X","O","X"],[7,"X",9]] :
			choix = 7
		if plateau == [[1,2,"O"],[4,"O","X"],["X","X",9]] :
			choix = 9
		if plateau == [["X",2,"O"],[4,"O","X"],["X","X","O"]] :
			choix = 4
		if plateau == [[1,"X","O"],[4,"O","X"],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,"O"],["X","O","X"],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,"O"],[4,"O","X"],[7,"X","X"]] :
			choix = 7	
		if plateau == [[1,2,3],[4,"O","X"],[7,8,"X"]] :
			choix = 3
		if plateau == [["X",2,"O"],[4,"O","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [[1,"X","O"],[4,"O","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [[1,2,"O"],["X","O","X"],[7,8,"X"]] :
			choix = 7
		if plateau == [[1,2,"O"],[4,"O","X"],["X",8,"X"]] :
			choix = 8
		if plateau == [["X",2,"O"],[4,"O","X"],["X","O","X"]] :
			choix = 2
		if plateau == [[1,"X","O"],[4,"O","X"],["X","O","X"]] :
			choix = 1
		if plateau == [[1,2,"O"],["X","O","X"],["X","O","X"]] :
			choix = 2	
		if plateau == [[1,2,3],[4,5,6],["X",8,9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"O",6],["X","X",9]] :
			choix = 9
		if plateau == [["X",2,3],[4,"O",6],["X","X","O"]] :
			choix = 4
		if plateau == [["X","X",3],["O","O",6],["X","X","O"]] :
			choix = 6
		if plateau == [["X",2,"X"],["O","O",6],["X","X","O"]] :
			choix = 6
		if plateau == [["X",2,3],["O","O","X"],["X","X","O"]] :
			choix = 3
		if plateau == [[1,"X",3],[4,"O",6],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,"X"],[4,"O",6],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,3],["X","O",6],["X","X","O"]] :
			choix = 1
		if plateau == [[1,2,3],[4,"O","X"],["X","X","O"]] :
			choix = 1	
		if plateau == [[1,2,3],[4,"O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["X",2,3],[4,"O",6],["X","O","X"]] :
			choix = 2
		if plateau == [[1,"X",3],[4,"O",6],["X","O","X"]] :
			choix = 4
		if plateau == [["X","X",3],["O","O",6],["X","O","X"]] :
			choix = 6
		if plateau == [[1,"X","X"],["O","O",6],["X","O","X"]] :
			choix = 6
		if plateau == [[1,"X",3],["O","O","X"],["X","O","X"]] :
			choix = 3
		if plateau == [[1,2,"X"],[4,"O",6],["X","O","X"]] :
			choix = 2
		if plateau == [[1,2,3],["X","O",6],["X","O","X"]] :
			choix = 2
		if plateau == [[1,2,3],[4,"O","X"],["X","O","X"]] :
			choix = 2
		if plateau == [[1,2,3],[4,5,6],[7,"X",9]] :
			choix = 5
		if plateau == [[1,2,3],[4,"O",6],[7,"X","X"]] :
			choix = 7
		if plateau == [["X",2,3],[4,"O",6],["O","X","X"]] :
			choix = 3
		if plateau == [[1,"X",3],[4,"O",6],["O","X","X"]] :
			choix = 3
		if plateau == [[1,2,"X"],[4,"O",6],["O","X","X"]] :
			choix = 6
		if plateau == [["X",2,"X"],[4,"O","O"],["O","X","X"]] :
			choix = 4
		if plateau == [[1,"X","X"],[4,"O","O"],["O","X","X"]] :
			choix = 4
		if plateau == [[1,2,"X"],["X","O","O"],["O","X","X"]] :
			choix = 1
		if plateau == [[1,2,3],["X","O",6],["O","X","X"]] :
			choix = 3
		if plateau == [[1,2,3],[4,"O","X"],["O","X","X"]] :
			choix = 3	
		if plateau == [[1,2,3],[4,5,6],[7,8,"X"]] :
			choix = 5
	if premier_joueur == "IA" and symbole == "O" :
		if plateau == [[1,2,3],[4,5,6],[7,8,9]] :
			choix = 1
		if plateau == [["X","O",3],[4,5,6],[7,8,9]] :
			choix = 7		
		if plateau == [["X","O","O"],[4,5,6],["X",8,9]] :
			choix = 4		
		if plateau == [["X","O",3],["O",5,6],["X",8,9]] :
			choix = 9
		if plateau == [["X","O","O"],["O",5,6],["X",8,"X"]] :	
			choix = 5
		if plateau == [["X","O",3],["O","O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["X","O",3],["O",5,"O"],["X",8,"X"]] :
			choix = 5
		if plateau == [["X","O",3],["O",5,6],["X","O","X"]] :
			choix = 5	
		if plateau == [["X","O",3],[4,"O",6],["X",8,9]] :
			choix = 4		
		if plateau == [["X","O",3],[4,5,"O"],["X",8,9]] :
			choix = 4	
		if plateau == [["X","O",3],[4,5,6],["X","O",9]] :
			choix = 4	
		if plateau == [["X","O",3],[4,5,6],["X",8,"O"]] :
			choix = 4			
		if plateau == [["X",2,"O"],[4,5,6],[7,8,9]] :
			choix = 7
		if plateau == [["X",2,"O"],["O",5,6],["X",8,9]] :
			choix = 9
		if plateau == [["X",2,"O"],["O","O",6],["X",8,"X"]] :
			choix = 8
		if plateau == [["X",2,"O"],["O",5,"O"],["X",8,"X"]] :
			choix = 5
		if plateau == [["X",2,"O"],["O",5,6],["X","O","X"]] :
			choix = 5
		if plateau == [["X",2,"O"],[4,"O",6],["X",8,9]] :
			choix = 4	
		if plateau == [["X",2,"O"],[4,5,"O"],["X",8,9]] :
			choix = 4	
		if plateau == [["X",2,"O"],[4,5,6],["X","O",9]] :
			choix = 4	
		if plateau == [["X",2,"O"],[4,5,6],["X",8,"O"]] :
			choix = 4			
		if plateau == [["X",2,3],["O",5,6],[7,8,9]] :
			choix = 3
		if plateau == [["X","O","X"],["O",5,6],[7,8,9]] :
			choix = 9
		if plateau == [["X","O","X"],["O","O",6],[7,8,"X"]] : 
			choix = 6
		if plateau == [["X","O","X"],["O",5,"O"],[7,8,"X"]] :
			choix = 5
		if plateau == [["X","O","X"],["O",5,6],["O",8,"X"]] :
			choix = 5
		if plateau == [["X","O","X"],["O",5,6],[7,"O","X"]] :
			choix = 5		
		if plateau == [["X",2,"X"],["O","O",6],[7,8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],["O",5,"O"],[7,8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],["O",5,6],["O",8,9]] :
			choix = 2	
		if plateau == [["X",2,"X"],["O",5,6],[7,"O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],["O",5,6],[7,8,"O"]] :
			choix = 2			
		if plateau == [["X",2,3],[4,"O",6],[7,8,9]] :
			choix = 3	
		if plateau == [["X","O","X"],[4,"O",6],[7,8,9]] :
			choix = 8	
		if plateau == [["X","O","X"],["O","O",6],[7,"X",9]] :
			choix = 6	
		if plateau == [["X","O","X"],[4,"O","O"],[7,"X",9]] :
			choix = 4	
		if plateau == [["X","O","X"],[4,"O",6],["O","X",9]] :
			choix = 6		
		if plateau == [["X","O","X"],[4,"O",6],[7,"X","O"]] :
			choix = 4	
		if plateau == [["X",2,"X"],[4,"O","O"],[7,8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],["O",8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],[7,"O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,"O",6],[7,8,"O"]] :
			choix = 2		
		if plateau == [["X",2,3],[4,5,"O"],[7,8,9]] :
			choix = 3
		if plateau == [["X","O","X"],[4,5,"O"],[7,8,9]] :
			choix = 7
		if plateau == [["X","O","X"],["O",5,"O"],["X",8,9]] :
			choix = 5
		if plateau == [["X","O","X"],[4,"O","O"],["X",8,9]] :
			choix = 4
		if plateau == [["X","O","X"],[4,5,"O"],["X","O",9]] :
			choix = 5
		if plateau == [["X","O","X"],[4,5,"O"],["X",8,"O"]] :
			choix = 5	
		if plateau == [["X",2,"X"],[4,5,"O"],["O",8,9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,5,"O"],[7,"O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,5,"O"],[7,8,"O"]] :
			choix = 2
		if plateau == [["X",2,3],[4,5,6],["O",8,9]] :
			choix = 3
		if plateau == [["X","O","X"],[4,5,6],["O",8,9]] :
			choix = 9
		if plateau == [["X","O","X"],[4,"O",6],["O",8,"X"]] :
			choix = 6
		if plateau == [["X","O","X"],[4,5,"O"],["O",8,"X"]] :
			choix = 5
		if plateau == [["X","O","X"],[4,5,6],["O","O","X"]] :
			choix = 5
		if plateau == [["X",2,"X"],[4,5,6],["O","O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],[4,5,6],["O",8,"O"]] :
			choix = 2			
		if plateau == [["X",2,3],[4,5,6],[7,"O",9]] :
			choix = 7
		if plateau == [["X",2,3],["O",5,6],["X","O",9]] :
			choix = 3
		if plateau == [["X","O","X"],["O",5,6],["X","O",9]] :
			choix = 5
		if plateau == [["X",2,"X"],["O","O",6],["X","O",9]] :
			choix = 2
		if plateau == [["X",2,"X"],["O",5,"O"],["X","O",9]] :
			choix = 5
		if plateau == [["X",2,"X"],["O",5,6],["X","O","O"]] :
			choix = 5	
		if plateau == [["X",2,3],[4,"O",6],["X","O",9]] :
			choix = 4
		if plateau == [["X",2,3],[4,5,"O"],["X","O",9]] :
			choix = 4
		if plateau == [["X",2,3],[4,5,6],["X","O","O"]] :
			choix = 4		
		if plateau == [["X","O","X"],[4,5,6],[7,8,"O"]] :
			choix = 7
		if plateau == [["X","O","X"],["O",5,6],["X",8,"O"]] :
			choix = 5
		if plateau == [["X","O","X"],[4,"O",6],["X",8,"O"]] :
			choix = 4
		if plateau == [["X","O","X"],[4,5,6],["X","O","O"]] :
			choix = 5
		if plateau == [["X",2,3],[4,5,6],[7,8,"O"]] :
			choix = 3
		if plateau == [["X",2,"X"],[4,5,6],[7,"O","O"]] :
			choix = 2	
	if premier_joueur == "IA" and symbole == "X" :
		if plateau == [[1,2,3],[4,5,6],[7,8,9]] :
			choix = 1
		if plateau == [["O","X",3],[4,5,6],[7,8,9]] :
			choix = 7		
		if plateau == [["O","X","X"],[4,5,6],["O",8,9]] :
			choix = 4		
		if plateau == [["O","X",3],["X",5,6],["O",8,9]] :
			choix = 9
		if plateau == [["O","X","X"],["X",5,6],["O",8,"O"]] :	
			choix = 5
		if plateau == [["O","X",3],["X","X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["O","X",3],["X",5,"X"],["O",8,"O"]] :
			choix = 5
		if plateau == [["O","X",3],["X",5,6],["O","X","O"]] :
			choix = 5	
		if plateau == [["O","X",3],[4,"X",6],["O",8,9]] :
			choix = 4		
		if plateau == [["O","X",3],[4,5,"X"],["O",8,9]] :
			choix = 4	
		if plateau == [["O","X",3],[4,5,6],["O","X",9]] :
			choix = 4	
		if plateau == [["O","X",3],[4,5,6],["O",8,"X"]] :
			choix = 4			
		if plateau == [["O",2,"X"],[4,5,6],[7,8,9]] :
			choix = 7
		if plateau == [["O",2,"X"],["X",5,6],["O",8,9]] :
			choix = 9
		if plateau == [["O",2,"X"],["X","X",6],["O",8,"O"]] :
			choix = 8
		if plateau == [["O",2,"X"],["X",5,"X"],["O",8,"O"]] :
			choix = 5
		if plateau == [["O",2,"X"],["X",5,6],["O","X","O"]] :
			choix = 5
		if plateau == [["O",2,"X"],[4,"X",6],["O",8,9]] :
			choix = 4	
		if plateau == [["O",2,"X"],[4,5,"X"],["O",8,9]] :
			choix = 4	
		if plateau == [["O",2,"X"],[4,5,6],["O","X",9]] :
			choix = 4	
		if plateau == [["O",2,"X"],[4,5,6],["O",8,"X"]] :
			choix = 4			
		if plateau == [["O",2,3],["X",5,6],[7,8,9]] :
			choix = 3
		if plateau == [["O","X","O"],["X",5,6],[7,8,9]] :
			choix = 9
		if plateau == [["O","X","O"],["X","X",6],[7,8,"O"]] : 
			choix = 6
		if plateau == [["O","X","O"],["X",5,"X"],[7,8,"O"]] :
			choix = 5
		if plateau == [["O","X","O"],["X",5,6],["X",8,"O"]] :
			choix = 5
		if plateau == [["O","X","O"],["X",5,6],[7,"X","O"]] :
			choix = 5		
		if plateau == [["O",2,"O"],["X","X",6],[7,8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],["X",5,"X"],[7,8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],["X",5,6],["X",8,9]] :
			choix = 2	
		if plateau == [["O",2,"O"],["X",5,6],[7,"X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],["X",5,6],[7,8,"X"]] :
			choix = 2			
		if plateau == [["O",2,3],[4,"X",6],[7,8,9]] :
			choix = 3	
		if plateau == [["O","X","O"],[4,"X",6],[7,8,9]] :
			choix = 8	
		if plateau == [["O","X","O"],["X","X",6],[7,"O",9]] :
			choix = 6	
		if plateau == [["O","X","O"],[4,"X","X"],[7,"O",9]] :
			choix = 4	
		if plateau == [["O","X","O"],[4,"X",6],["X","O",9]] :
			choix = 6		
		if plateau == [["O","X","O"],[4,"X",6],[7,"O","X"]] :
			choix = 4	
		if plateau == [["O",2,"O"],[4,"X","X"],[7,8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],["X",8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],[7,"X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,"X",6],[7,8,"X"]] :
			choix = 2		
		if plateau == [["O",2,3],[4,5,"X"],[7,8,9]] :
			choix = 3
		if plateau == [["O","X","O"],[4,5,"X"],[7,8,9]] :
			choix = 7
		if plateau == [["O","X","O"],["X",5,"X"],["O",8,9]] :
			choix = 5
		if plateau == [["O","X","O"],[4,"X","X"],["O",8,9]] :
			choix = 4
		if plateau == [["O","X","O"],[4,5,"X"],["O","X",9]] :
			choix = 5
		if plateau == [["O","X","O"],[4,5,"X"],["O",8,"X"]] :
			choix = 5	
		if plateau == [["O",2,"O"],[4,5,"X"],["X",8,9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,5,"X"],[7,"X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,5,"X"],[7,8,"X"]] :
			choix = 2
		if plateau == [["O",2,3],[4,5,6],["X",8,9]] :
			choix = 3
		if plateau == [["O","X","O"],[4,5,6],["X",8,9]] :
			choix = 9
		if plateau == [["O","X","O"],[4,"X",6],["X",8,"O"]] :
			choix = 6
		if plateau == [["O","X","O"],[4,5,"X"],["X",8,"O"]] :
			choix = 5
		if plateau == [["O","X","O"],[4,5,6],["X","X","O"]] :
			choix = 5
		if plateau == [["O",2,"O"],[4,5,6],["X","X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],[4,5,6],["X",8,"X"]] :
			choix = 2			
		if plateau == [["O",2,3],[4,5,6],[7,"X",9]] :
			choix = 7
		if plateau == [["O",2,3],["X",5,6],["O","X",9]] :
			choix = 3
		if plateau == [["O","X","O"],["X",5,6],["O","X",9]] :
			choix = 5
		if plateau == [["O",2,"O"],["X","X",6],["O","X",9]] :
			choix = 2
		if plateau == [["O",2,"O"],["X",5,"X"],["O","X",9]] :
			choix = 5
		if plateau == [["O",2,"O"],["X",5,6],["O","X","X"]] :
			choix = 5	
		if plateau == [["O",2,3],[4,"X",6],["O","X",9]] :
			choix = 4
		if plateau == [["O",2,3],[4,5,"X"],["O","X",9]] :
			choix = 4
		if plateau == [["O",2,3],[4,5,6],["O","X","X"]] :
			choix = 4		
		if plateau == [["O","X","O"],[4,5,6],[7,8,"X"]] :
			choix = 7
		if plateau == [["O","X","O"],["X",5,6],["O",8,"X"]] :
			choix = 5
		if plateau == [["O","X","O"],[4,"X",6],["O",8,"X"]] :
			choix = 4
		if plateau == [["O","X","O"],[4,5,6],["O","X","X"]] :
			choix = 5
		if plateau == [["O",2,3],[4,5,6],[7,8,"X"]] :
			choix = 3
		if plateau == [["O",2,"O"],[4,5,6],[7,"X","X"]] :
			choix = 2
	return choix
	
def morpion() :
	
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	plateau_precedent = [[1,2,3],[4,5,6],[7,8,9]]
	premier_joueur = "joueur"
	joueur = "joueur"
	symbole = "O"
	print("Test IA morpion aleatoire")
	# Si vous voulez essayer la partie où le joueur 1 a choisi les O et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 1785 et 1787
	# Enlevez les # des lignes 1791 et 1793
	#'''
	symbole = "O"
	#'''
	# Si vous voulez essayer la partie où le joueur 1 a choisi les X et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 1791 et 1793
	# Enlevez les # des lignes 1785 et 1787
	'''
	symbole = "X"
	'''	
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 1797 et 1873
	# Enlevez les # des lignes 544 et 623
	'''	
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
	'''
	# Si vous voulez essayer la partie où le joueur commence et si les instructions suivantes n'ont pas déjà été effectuées :
	# Mettez des # avant les 3 apostrophes des lignes 1797 et 1873
	# Enlevez les # des lignes 1797 et 1873
	#'''
	premier_joueur = "IA"
	joueur = "IA"
	if premier_joueur == "IA" :
		choix1 = decision(plateau,joueur,premier_joueur,symbole)
		plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix1)
		plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix1)
		joueur = changer(joueur)
		for a in [1,2,3,4,5,6,7,8,9] :
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
											choix8 = d
											plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix8)
											if plateau != plateau_precedent :
												plateau_precedent = mettre_valeur(joueur,premier_joueur,symbole,plateau_precedent,choix8)
												joueur = changer(joueur)
												choix9 = decision(plateau,joueur,premier_joueur,symbole)
												plateau = traduction(joueur,premier_joueur,symbole,plateau,plateau_precedent,choix9)
												joueur = changer(joueur)
												plateau = enlever(choix8,plateau)
												plateau_precedent = enlever(choix8,plateau_precedent)			
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
	#'''
		
morpion()
