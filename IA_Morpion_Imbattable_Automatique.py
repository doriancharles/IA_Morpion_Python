#Affiche les 3 valeurs de chaque lignes, dans l'ordre, lignes par lignes.
def afficher(plateau) :
	
	for i in range(0,len(plateau)) :
		print(plateau[i])
	print("")

#Vérifie que le joueur actuel a les ronds et retourne True si c'est le cas.	
def aLesRonds(joueur,premier_joueur,symbole) :
	
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "O" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "X") :
		return True		

#Met le symbole du joueur actuel à une place correspondante à un choix valide puis vérifie si il a gagné ou si il y a égalité.		
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"
	else :
		plateau[ligne][colonne] = "X"
	if joueur == "IA" :
		print("L'IA a joué")
		print("")
	if joueur == "joueur" :
		print("Vous avez les ",symbole)
		print("")
	if estVictorieux(plateau) == True :		
		victoire(premier_joueur,joueur,plateau)	
	if estEgalitaire(plateau) == True :	
		remplir(plateau,symbole,joueur,premier_joueur)		
		if estVictorieux(plateau) == True :			
			joueur = changer(joueur)
			victoire(premier_joueur,joueur,plateau)			
		egalite()		
	afficher(plateau)
	return plateau

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.	
def estPossible(joueur,plateau,symbole,ligne,colonne) :
	
	if joueur == "IA" :
		if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
			return False	
	if joueur == "joueur" :
		if symbole == "O" :
			if plateau[ligne][colonne] == "O" :
				print("Vous avez déjà choisi cette case")
				print("")
				return False	
			if plateau[ligne][colonne] == "X" :
				print("L'IA a déjà choisie cette case")
				print("")
				return False									
		if symbole == "X" :						
			if plateau[ligne][colonne] == "O" :								
				print("L'IA a déjà choisie cette case")
				print("")
				return False									
			if plateau[ligne][colonne] == "X" :								
				print("Vous avez déjà choisi cette case")
				print("")
				return False	

#Traduit un choix en coordonnées (ligne et colonne) qu'il retourne dans une liste.								
def traduction(choix) :	
	
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
	
def verification_demande(joueur,plateau,premier_joueur,symbole) :
			
	choix = 0	
	while choix not in ('1','2','3','4','5','6','7','8','9') :		
		afficher(plateau)
		choix = input("Choisissez un emplacement en écrivant le chiffre le représentant : ")
		print("")				
	choix = int(choix)
	coordonnees = traduction(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	if estPossible(joueur,plateau,symbole,ligne,colonne) == False :				
		verification_demande(joueur,plateau,premier_joueur,symbole)
	else :
		placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne) 
	return plateau

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(plateau) :
	
	afficher(plateau)
	print("L'IA a gagné")
	print("")
	morpion()

#Affiche qu'il y a égalité.			
def egalite() :
	
	print("Il y a égalité.")
	print("")
	morpion()

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

#Compte le nombre de cases complétées et retourne True si il y en a 8.		
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(0,len(plateau)) :
		for j in range(0,len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 8 :
		return True			

def decision(plateau,joueur,symbole,premier_joueur) :
	
	exemple = plateau
	while exemple == plateau :
		if premier_joueur == "joueur" and symbole == "O" or premier_joueur == "IA" and symbole == "O" :
			if plateau == [["O",2,3],[4,"X","O"],[7,8,9]] :
				plateau = [["O",2,3],[4,"X","O"],[7,"X",9]]
				break
			if plateau == [["O",2,3],[4,"X",6],[7,"O",9]] :
				plateau = [["O",2,3],[4,"X","X"],[7,"O",9]]
				break
			if plateau == [[1,2,"O"],["O","X",6],[7,8,9]] :
				plateau = [[1,2,"O"],["O","X",6],[7,"X",9]] 
				break
			if plateau == [[1,2,"O"],[4,"X",6],[7,"O",9]] :
				plateau = [[1,2,"O"],["X","X",6],[7,"O",9]]
				break
			if plateau == [[1,"O",3],[4,"X",6],["O",8,9]] :
				plateau = [[1,"O",3],[4,"X","X"],["O",8,9]]
				break
			if plateau == [[1,2,3],[4,"X","O"],["O",8,9]] :
				plateau = [[1,"X",3],[4,"X","O"],["O",8,9]]
				break 
			if plateau == [[1,"O",3],[4,"X",6],[7,8,"O"]] :
				plateau = [[1,"O",3],["X","X",6],[7,8,"O"]]
				break
			if plateau == [[1,2,3],["O","X",6],[7,8,"O"]] :
				plateau = [[1,"X",3],["O","X",6],[7,8,"O"]]
				break		
			if plateau == [[1,"O",3],[4,"X",6],[7,"O",9]] :
				plateau = [["X","O",3],[4,"X",6],[7,"O",9]]
				break 
			if plateau == [[1,2,3],["O","X","O"],[7,8,9]] :
				plateau = [["X",2,3],["O","X","O"],[7,8,9]]
				break		
			if plateau == [["O",2,3],[4,"X",6],[7,8,"O"]] :
				plateau = [["O","X",3],[4,"X",6],[7,8,"O"]]
				break 
			if plateau == [[1,2,"O"],[4,"X",6],["O",8,9]] :
				plateau = [[1,"X","O"],[4,"X",6],["O",8,9]] 
				break		
			if plateau == [[1,"O",3],["O","X",6],[7,8,9]] :
				plateau = [[1,"O","X"],["O","X",6],[7,8,9]]
				break
			if plateau == [[1,"O",3],[4,"X","O"],[7,8,9]] :
				plateau = [["X","O",3],[4,"X","O"],[7,8,9]]
				break
			if plateau == [[1,2,3],["O","X",6],[7,"O",9]] :
				plateau = [["X",2,3],["O","X",6],[7,"O",9]]
				break
			if plateau == [[1,2,3],[4,"X","O"],[7,"O",9]] :
				plateau = [[1,2,"X"],[4,"X","O"],[7,"O",9]]
				break		
			if plateau == [["O","O","X"],["X","X","O"],["O",8,9]] :	
				plateau = [["O","O","X"],["X","X","O"],["O",8,"X"]]
				break
			if plateau == [["X","O","O"],["O","X","X"],[7,8,"O"]] :
				plateau = [["X","O","O"],["O","X","X"],["X",8,"O"]]
				break
			if plateau == [["O","X","O"],["O","X",6],["X","O",9]] :
				plateau = [["O","X","O"],["O","X",6],["X","O","X"]]
				break
			if plateau == [["O","X","O"],[4,"X","O"],[7,"O","X"]] :
				plateau = [["O","X","O"],[4,"X","O"],["X","O","X"]]
				break
			if plateau == [["X","O",3],["O","X",6],["O","X","O"]] :
				plateau = [["X","O","X"],["O","X",6],["O","X","O"]]
				break
			if plateau == [[1,"O","X"],[4,"X","O"],["O","X","O"]] :
				plateau = [["X","O","X"],[4,"X","O"],["O","X","O"]]
				break
			if plateau == [["O",2,3],["X","X","O"],["O","O","X"]] :
				plateau = [["O",2,"X"],["X","X","O"],["O","O","X"]]
				break
			if plateau == [[1,2,"O"],["O","X","X"],["X","O","O"]] :
				plateau = [["X",2,"O"],["O","X","X"],["X","O","O"]]
				break			
			if plateau == [["O","X","O"],[4,"X",6],[7,"O",9]] :
				plateau = [["O","X","O"],["X","X",6],[7,"O",9]]
				break
			if plateau == [["O",2,3],["X","X","O"],["O",8,9]] :
				plateau = [["O","X",3],["X","X","O"],["O",8,9]]
				break
			if plateau == [[1,2,"O"],["O","X","X"],[7,8,"O"]] :
				plateau = [[1,"X","O"],["O","X","X"],[7,8,"O"]]
				break
			if plateau == [[1,"O",3],[4,"X",6],["O","X","O"]] :
				plateau = [[1,"O",3],["X","X",6],["O","X","O"]]
				break			
			if plateau == [["X","O",3],["O","O","X"],[7,"X","O"]] :
				plateau = [["X","O","X"],["O","O","X"],[7,"X","O"]]
				break
			if plateau == [["X","O","X"],[4,"O",6],["O","X","O"]] :
				plateau = [["X","O","X"],["X","O",6],["O","X","O"]]
				break
			if plateau == [["X","O",3],[4,"O",6],[7,"X","O"]] :
				plateau = [["X","O",3],["X","O",6],[7,"X","O"]]
				break			
			if plateau == [["X",2,"O"],["O","O","X"],["X",8,"O"]] :
				plateau = [["X","X","O"],["O","O","X"],["X",8,"O"]]
				break			
			if plateau == [["X",2,3],["O","O","X"],[7,8,"O"]] :
				plateau = [["X","X",3],["O","O","X"],[7,8,"O"]]
				break			
			if plateau == [["X",2,3],[4,"O",6],[7,8,"O"]] :
				plateau = [["X",2,"X"],[4,"O",6],[7,8,"O"]]
				break		
			if plateau[0][0] == "X" and plateau[0][1] == "X" and plateau[0][2] == 3 :
				plateau[0][2] = "X"
				break
			if plateau[0][0] == "X" and plateau[0][1] == 2 and plateau[0][2] == "X" :
				plateau[0][1] = "X"
				break
			if plateau[0][0] == 1 and plateau[0][1] == "X" and plateau[0][2] == "X" :		
				plateau[0][0] = "X"
				break		
			if plateau[1][0] == "X" and plateau[1][1] == "X" and plateau[1][2] == 6 :
				plateau[1][2] = "X"
				break
			if plateau[1][0] == "X" and plateau[1][1] == 5 and plateau[1][2] == "X" :	
				plateau[1][1] = "X"
				break
			if plateau[1][0] == 4 and plateau[1][1] == "X" and plateau[1][2] == "X" :
				plateau[1][0] = "X"
				break
			if plateau[2][0] == "X" and plateau[2][1] == "X" and plateau[2][2] == 9 :
				plateau[2][2] = "X"
				break
			if plateau[2][0] == "X" and plateau[2][1] == 8 and plateau[2][2] == "X" :
				plateau[2][1] = "X"
				break
			if plateau[2][0] == 7 and plateau[2][1] == "X" and plateau[2][2] == "X" :
				plateau[2][0] = "X"
				break				
			if plateau[0][0] == "X" and plateau[1][0] == "X" and plateau[2][0] == 7 :		
				plateau[2][0] = "X"
				break
			if plateau[0][0] == "X" and plateau[1][0] == 4 and plateau[2][0] == "X" :	
				plateau[1][0] = "X"
				break
			if plateau[0][0] == 1 and plateau[1][0] == "X" and plateau[2][0] == "X" :
				plateau[0][0] = "X"
				break			
			if plateau[0][1] == "X" and plateau[1][1] == "X" and plateau[2][1] == 8 :
				plateau[2][1] = "X"
				break
			if plateau[0][1] == "X" and plateau[1][1] == 5 and plateau[2][1] == "X" :
				plateau[1][1] = "X"
				break
			if plateau[0][1] == 2 and plateau[1][1] == "X" and plateau[2][1] == "X" :
				plateau[0][1] = "X"
				break			
			if plateau[0][2] == "X" and plateau[1][2] == "X" and plateau[2][2] == 9 :
				plateau[2][2] = "X"
				break
			if plateau[0][2] == "X" and plateau[1][2] == 6 and plateau[2][2] == "X" :
				plateau[1][2] = "X"
				break
			if plateau[0][2] == 3 and plateau[1][2] == "X" and plateau[2][2] == "X" :
				plateau[0][2] = "X"
				break				
			if plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == 9 :	
				plateau[2][2] = "X"
				break
			if plateau[0][0] == "X" and plateau[1][1] == 5 and plateau[2][2] == "X" :
				plateau[1][1] = "X"
				break
			if plateau[0][0] == 1 and plateau[1][1] == "X" and plateau[2][2] == "X" :
				plateau[0][0] = "X"	
				break				
			if plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == 7 :
				plateau[2][0] = "X"	
				break	
			if plateau[0][2] == "X" and plateau[1][1] == 5 and plateau[2][0] == "X" :
				plateau[1][1] = "X"
				break
			if plateau[0][2] == 3 and plateau[1][1] == "X" and plateau[2][0] == "X" :
				plateau[0][2] = "X"
				break			
			if plateau[0][0] == "O" and plateau[0][1] == "O" and plateau[0][2] == 3 :
				plateau[0][2] = "X"
				break
			if plateau[0][0] == "O" and plateau[0][1] == 2 and plateau[0][2] == "O" :
				plateau[0][1] = "X"
				break
			if plateau[0][0] == 1 and plateau[0][1] == "O" and plateau[0][2] == "O" :		
				plateau[0][0] = "X"
				break				
			if plateau[1][0] == "O" and plateau[1][1] == "O" and plateau[1][2] == 6 :
				plateau[1][2] = "X"
				break
			if plateau[1][0] == "O" and plateau[1][1] == 5 and plateau[1][2] == "O" :	
				plateau[1][1] = "X"
				break
			if plateau[1][0] == 4 and plateau[1][1] == "O" and plateau[1][2] == "O" :
				plateau[1][0] = "X"
				break				
			if plateau[2][0] == "O" and plateau[2][1] == "O" and plateau[2][2] == 9 :
				plateau[2][2] = "X"
				break
			if plateau[2][0] == "O" and plateau[2][1] == 8 and plateau[2][2] == "O" :
				plateau[2][1] = "X"
				break
			if plateau[2][0] == 7 and plateau[2][1] == "O" and plateau[2][2] == "O" :
				plateau[2][0] = "X"
				break					
			if plateau[0][0] == "O" and plateau[1][0] == "O" and plateau[2][0] == 7 :		
				plateau[2][0] = "X"
				break
			if plateau[0][0] == "O" and plateau[1][0] == 4 and plateau[2][0] == "O" :	
				plateau[1][0] = "X"
				break
			if plateau[0][0] == 1 and plateau[1][0] == "O" and plateau[2][0] == "O" :
				plateau[0][0] = "X"
				break				
			if plateau[0][1] == "O" and plateau[1][1] == "O" and plateau[2][1] == 8 :
				plateau[2][1] = "X"
				break
			if plateau[0][1] == "O" and plateau[1][1] == 5 and plateau[2][1] == "O" :
				plateau[1][1] = "X"
				break
			if plateau[0][1] == 2 and plateau[1][1] == "O" and plateau[2][1] == "O" :
				plateau[0][1] = "X"
				break				
			if plateau[0][2] == "O" and plateau[1][2] == "O" and plateau[2][2] == 9 :
				plateau[2][2] = "X"
				break
			if plateau[0][2] == "O" and plateau[1][2] == 6 and plateau[2][2] == "O" :
				plateau[1][2] = "X"
				break
			if plateau[0][2] == 3 and plateau[1][2] == "O" and plateau[2][2] == "O" :
				plateau[0][2] = "X"
				break					
			if plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == 9 :	
				plateau[2][2] = "X"
				break
			if plateau[0][0] == "O" and plateau[1][1] == 5 and plateau[2][2] == "O" :
				plateau[1][1] = "X"
				break
			if plateau[0][0] == 1 and plateau[1][1] == "O" and plateau[2][2] == "O" :
				plateau[0][0] = "X"	
				break						
			if plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == 7 :
				plateau[2][0] = "X"	
				break	
			if plateau[0][2] == "O" and plateau[1][1] == 5 and plateau[2][0] == "O" :
				plateau[1][1] = "X"
				break
			if plateau[0][2] == 3 and plateau[1][1] == "O" and plateau[2][0] == "O" :
				plateau[0][2] = "X"
				break		
		if premier_joueur == "joueur" and symbole == "X" or premier_joueur == "IA" and symbole == "X" :
			if plateau == [["X",2,3],[4,"O","X"],[7,8,9]] :
				plateau = [["X",2,3],[4,"O","X"],[7,"O",9]]
				break
			if plateau == [["X",2,3],[4,"O",6],[7,"X",9]] :
				plateau = [["X",2,3],[4,"O","O"],[7,"X",9]]
				break
			if plateau == [[1,2,"X"],["X","O",6],[7,8,9]] :
				plateau = [[1,2,"X"],["X","O",6],[7,"O",9]] 
				break
			if plateau == [[1,2,"X"],[4,"O",6],[7,"X",9]] :
				plateau = [[1,2,"X"],["O","O",6],[7,"X",9]]
				break
			if plateau == [[1,"X",3],[4,"O",6],["X",8,9]] :
				plateau = [[1,"X",3],[4,"O","O"],["X",8,9]]
				break
			if plateau == [[1,2,3],[4,"O","X"],["X",8,9]] :
				plateau = [[1,"O",3],[4,"O","X"],["X",8,9]]
				break 
			if plateau == [[1,"X",3],[4,"O",6],[7,8,"X"]] :
				plateau = [[1,"X",3],["O","O",6],[7,8,"X"]]
				break
			if plateau == [[1,2,3],["X","O",6],[7,8,"X"]] :
				plateau = [[1,"O",3],["X","O",6],[7,8,"X"]]
				break		
			if plateau == [[1,"X",3],[4,"O",6],[7,"X",9]] :
				plateau = [["O","X",3],[4,"O",6],[7,"X",9]]
				break 
			if plateau == [[1,2,3],["X","O","X"],[7,8,9]] :
				plateau = [["O",2,3],["X","O","X"],[7,8,9]]
				break		
			if plateau == [["X",2,3],[4,"O",6],[7,8,"X"]] :
				plateau = [["X","O",3],[4,"O",6],[7,8,"X"]]
				break 
			if plateau == [[1,2,"X"],[4,"O",6],["X",8,9]] :
				plateau = [[1,"O","X"],[4,"O",6],["X",8,9]] 
				break		
			if plateau == [[1,"X",3],["X","O",6],[7,8,9]] :
				plateau = [[1,"X","O"],["X","O",6],[7,8,9]]
				break
			if plateau == [[1,"X",3],[4,"O","X"],[7,8,9]] :
				plateau = [["O","X",3],[4,"O","X"],[7,8,9]]
				break
			if plateau == [[1,2,3],["X","O",6],[7,"X",9]] :
				plateau = [["O",2,3],["X","O",6],[7,"X",9]]
				break
			if plateau == [[1,2,3],[4,"O","X"],[7,"X",9]] :
				plateau = [[1,2,"O"],[4,"O","X"],[7,"X",9]]
				break		
			if plateau == [["X","X","O"],["O","O","X"],["X",8,9]] :	
				plateau = [["X","X","O"],["O","O","X"],["X",8,"O"]]
				break
			if plateau == [["O","X","X"],["X","O","O"],[7,8,"X"]] :
				plateau = [["O","X","X"],["X","O","O"],["O",8,"X"]]
				break
			if plateau == [["X","O","X"],["X","O",6],["O","X",9]] :
				plateau = [["X","O","X"],["X","O",6],["O","X","O"]]
				break
			if plateau == [["X","O","X"],[4,"O","X"],[7,"X","O"]] :
				plateau = [["X","O","X"],[4,"O","X"],["O","X","O"]]
				break
			if plateau == [["O","X",3],["X","O",6],["X","O","X"]] :
				plateau = [["O","X","O"],["X","O",6],["X","O","X"]]
				break
			if plateau == [[1,"X","O"],[4,"O","X"],["X","O","X"]] :
				plateau = [["O","X","O"],[4,"O","X"],["X","O","X"]]
				break
			if plateau == [["X",2,3],["O","O","X"],["X","X","O"]] :
				plateau = [["X",2,"O"],["O","O","X"],["X","X","O"]]
				break
			if plateau == [[1,2,"X"],["X","O","O"],["O","X","X"]] :
				plateau = [["O",2,"X"],["X","O","O"],["O","X","X"]]
				break			
			if plateau == [["X","O","X"],[4,"O",6],[7,"X",9]] :
				plateau = [["X","O","X"],["O","O",6],[7,"X",9]]
				break
			if plateau == [["X",2,3],["O","O","X"],["X",8,9]] :
				plateau = [["X","O",3],["O","O","X"],["X",8,9]]
				break
			if plateau == [[1,2,"X"],["X","O","O"],[7,8,"X"]] :
				plateau = [[1,"O","X"],["X","O","O"],[7,8,"X"]]
				break
			if plateau == [[1,"X",3],[4,"O",6],["X","O","X"]] :
				plateau = [[1,"X",3],["O","O",6],["X","O","X"]]
				break			
			if plateau == [["O","X",3],["X","X","O"],[7,"O","X"]] :
				plateau = [["O","X","O"],["X","X","O"],[7,"O","X"]]
				break
			if plateau == [["O","X","O"],[4,"X",6],["X","O","X"]] :
				plateau = [["O","X","O"],["O","X",6],["X","O","X"]]
				break
			if plateau == [["O","X",3],[4,"X",6],[7,"O","X"]] :
				plateau = [["O","X",3],["O","X",6],[7,"O","X"]]
				break			
			if plateau == [["O",2,"X"],["X","X","O"],["O",8,"X"]] :
				plateau = [["O","O","X"],["X","X","O"],["O",8,"X"]]
				break			
			if plateau == [["O",2,3],["X","X","O"],[7,8,"X"]] :
				plateau = [["O","O",3],["X","X","O"],[7,8,"X"]]
				break			
			if plateau == [["O",2,3],[4,"X",6],[7,8,"X"]] :
				plateau = [["O",2,"O"],[4,"X",6],[7,8,"X"]]
				break		
			if plateau[0][0] == "O" and plateau[0][1] == "O" and plateau[0][2] == 3 :
				plateau[0][2] = "O"
				break
			if plateau[0][0] == "O" and plateau[0][1] == 2 and plateau[0][2] == "O" :
				plateau[0][1] = "O"
				break
			if plateau[0][0] == 1 and plateau[0][1] == "O" and plateau[0][2] == "O" :		
				plateau[0][0] = "O"
				break		
			if plateau[1][0] == "O" and plateau[1][1] == "O" and plateau[1][2] == 6 :
				plateau[1][2] = "O"
				break
			if plateau[1][0] == "O" and plateau[1][1] == 5 and plateau[1][2] == "O" :	
				plateau[1][1] = "O"
				break
			if plateau[1][0] == 4 and plateau[1][1] == "O" and plateau[1][2] == "O" :
				plateau[1][0] = "O"
				break
			if plateau[2][0] == "O" and plateau[2][1] == "O" and plateau[2][2] == 9 :
				plateau[2][2] = "O"
				break
			if plateau[2][0] == "O" and plateau[2][1] == 8 and plateau[2][2] == "O" :
				plateau[2][1] = "O"
				break
			if plateau[2][0] == 7 and plateau[2][1] == "O" and plateau[2][2] == "O" :
				plateau[2][0] = "O"
				break				
			if plateau[0][0] == "O" and plateau[1][0] == "O" and plateau[2][0] == 7 :		
				plateau[2][0] = "O"
				break
			if plateau[0][0] == "O" and plateau[1][0] == 4 and plateau[2][0] == "O" :	
				plateau[1][0] = "O"
				break
			if plateau[0][0] == 1 and plateau[1][0] == "O" and plateau[2][0] == "O" :
				plateau[0][0] = "O"
				break			
			if plateau[0][1] == "O" and plateau[1][1] == "O" and plateau[2][1] == 8 :
				plateau[2][1] = "O"
				break
			if plateau[0][1] == "O" and plateau[1][1] == 5 and plateau[2][1] == "O" :
				plateau[1][1] = "O"
				break
			if plateau[0][1] == 2 and plateau[1][1] == "O" and plateau[2][1] == "O" :
				plateau[0][1] = "O"
				break			
			if plateau[0][2] == "O" and plateau[1][2] == "O" and plateau[2][2] == 9 :
				plateau[2][2] = "O"
				break
			if plateau[0][2] == "O" and plateau[1][2] == 6 and plateau[2][2] == "O" :
				plateau[1][2] = "O"
				break
			if plateau[0][2] == 3 and plateau[1][2] == "O" and plateau[2][2] == "O" :
				plateau[0][2] = "O"
				break				
			if plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == 9 :	
				plateau[2][2] = "O"
				break
			if plateau[0][0] == "O" and plateau[1][1] == 5 and plateau[2][2] == "O" :
				plateau[1][1] = "O"
				break
			if plateau[0][0] == 1 and plateau[1][1] == "O" and plateau[2][2] == "O" :
				plateau[0][0] = "O"	
				break				
			if plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == 7 :
				plateau[2][0] = "O"	
				break	
			if plateau[0][2] == "O" and plateau[1][1] == 5 and plateau[2][0] == "O" :
				plateau[1][1] = "O"
				break
			if plateau[0][2] == 3 and plateau[1][1] == "O" and plateau[2][0] == "O" :
				plateau[0][2] = "O"
				break			
			if plateau[0][0] == "X" and plateau[0][1] == "X" and plateau[0][2] == 3 :
				plateau[0][2] = "O"
				break
			if plateau[0][0] == "X" and plateau[0][1] == 2 and plateau[0][2] == "X" :
				plateau[0][1] = "O"
				break
			if plateau[0][0] == 1 and plateau[0][1] == "X" and plateau[0][2] == "X" :		
				plateau[0][0] = "O"
				break				
			if plateau[1][0] == "X" and plateau[1][1] == "X" and plateau[1][2] == 6 :
				plateau[1][2] = "O"
				break
			if plateau[1][0] == "X" and plateau[1][1] == 5 and plateau[1][2] == "X" :	
				plateau[1][1] = "O"
				break
			if plateau[1][0] == 4 and plateau[1][1] == "X" and plateau[1][2] == "X" :
				plateau[1][0] = "O"
				break				
			if plateau[2][0] == "X" and plateau[2][1] == "X" and plateau[2][2] == 9 :
				plateau[2][2] = "O"
				break
			if plateau[2][0] == "X" and plateau[2][1] == 8 and plateau[2][2] == "X" :
				plateau[2][1] = "O"
				break
			if plateau[2][0] == 7 and plateau[2][1] == "X" and plateau[2][2] == "X" :
				plateau[2][0] = "O"
				break					
			if plateau[0][0] == "X" and plateau[1][0] == "X" and plateau[2][0] == 7 :		
				plateau[2][0] = "O"
				break
			if plateau[0][0] == "X" and plateau[1][0] == 4 and plateau[2][0] == "X" :	
				plateau[1][0] = "O"
				break
			if plateau[0][0] == 1 and plateau[1][0] == "X" and plateau[2][0] == "X" :
				plateau[0][0] = "O"
				break				
			if plateau[0][1] == "X" and plateau[1][1] == "X" and plateau[2][1] == 8 :
				plateau[2][1] = "O"
				break
			if plateau[0][1] == "X" and plateau[1][1] == 5 and plateau[2][1] == "X" :
				plateau[1][1] = "O"
				break
			if plateau[0][1] == 2 and plateau[1][1] == "X" and plateau[2][1] == "X" :
				plateau[0][1] = "O"
				break				
			if plateau[0][2] == "X" and plateau[1][2] == "X" and plateau[2][2] == 9 :
				plateau[2][2] = "O"
				break
			if plateau[0][2] == "X" and plateau[1][2] == 6 and plateau[2][2] == "X" :
				plateau[1][2] = "O"
				break
			if plateau[0][2] == 3 and plateau[1][2] == "X" and plateau[2][2] == "X" :
				plateau[0][2] = "O"
				break					
			if plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == 9 :	
				plateau[2][2] = "O"
				break
			if plateau[0][0] == "X" and plateau[1][1] == 5 and plateau[2][2] == "X" :
				plateau[1][1] = "O"
				break
			if plateau[0][0] == 1 and plateau[1][1] == "X" and plateau[2][2] == "X" :
				plateau[0][0] = "O"	
				break						
			if plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == 7 :
				plateau[2][0] = "O"	
				break	
			if plateau[0][2] == "X" and plateau[1][1] == 5 and plateau[2][0] == "X" :
				plateau[1][1] = "O"
				break
			if plateau[0][2] == 3 and plateau[1][1] == "X" and plateau[2][0] == "X" :
				plateau[0][2] = "O"
				break	
	if estEgalitaire(plateau) == True :
		print("L'IA a les croix")
		joueur = "IA"
		afficher(plateau)
		remplir(plateau,symbole,joueur,premier_joueur)
		egalite()	
	return plateau

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
	premier_joueur = "joueur"
	joueur = "joueur"
	reponse = "a"
	symbole = "a"
	print("IA morpion imbattable automatique")
	print("")
	while not reponse == "O" and reponse != "N" or not reponse != "O" and reponse == "N" :
		reponse = input("Appuyez sur O puis Entrée si vous voulez commencer ou N puis Entrée si vous ne voulez pas : ")
		print("")
	while not symbole == "O" and symbole != "X" or not symbole != "O" and symbole == "X" :
		symbole = input("Appuyez sur O si vous voulez les O ou X puis Entrée si vous voulez les X : ")
		print("")
	if reponse == "N" :
		premier_joueur = "IA"
	if reponse == "O" :
		choix = verification_demande(joueur,plateau,premier_joueur,symbole)
		if choix == 5 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,0)
		else :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1)
		while estVictorieux(plateau) != True :
			if premier_joueur == "IA" :		
				plateau = decision(plateau,"IA",symbole,premier_joueur)		
			plateau = verification_demande(joueur,plateau,premier_joueur,symbole)	
			if premier_joueur == "joueur" :		
				plateau = decision(plateau,"IA",symbole,premier_joueur)
	if reponse == "N" :
		placer_valeur("IA",premier_joueur,symbole,plateau,1,1)
		choix = verification_demande(joueur,plateau,premier_joueur,symbole)
		if choix == 1 or choix == 3 :
			placer_valeur("IA",premier_joueur,symbole,plateau,2,1)
		if choix == 2 or choix == 4 :
			placer_valeur("IA",premier_joueur,symbole,plateau,2,2)
		if choix == 6 or choix == 8 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,0)
		if choix == 7 or choix == 9 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,1)
		while estVictorieux(plateau) != True :
			if premier_joueur == "IA" :		
				plateau = decision(plateau,"IA",symbole,premier_joueur)	
			plateau = verification_demande(joueur,plateau,premier_joueur,symbole)	
			if premier_joueur == "joueur" :		
				plateau = decision(plateau,"IA",symbole,premier_joueur)
			
morpion()		
