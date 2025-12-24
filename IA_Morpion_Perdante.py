from random import randint

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
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"	
	else :
		plateau[ligne][colonne] = "X"	
	if joueur == "IA" :
		print("L'IA a joué ",choix)
		print("")	
	else :
		print("Vous avez les ",symbole)
		print("")
	if estVictorieux(joueur,premier_joueur,symbole,plateau) == True :
		victoire(joueur,plateau,reponse)
	if estEgalitaire(plateau) == True :
		remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
		if estVictorieux(joueur,premier_joueur,symbole,plateau) == True :
			joueur = changer(joueur)
			victoire(joueur,plateau,reponse)
		egalite()
	afficher(plateau)

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.	
def estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,reponse,tour,dejavu) :
		
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
	if joueur == "IA" :
		if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
			return False
		obligation(tour,dejavu,plateau,symbole,joueur,premier_joueur,reponse)
		if empecheVictoire(premier_joueur,symbole,choix,plateau) == True :
			return False
	else :
		return True

#Traduit un choix en coordonnées (ligne et colonne) qu'il retourne dans une liste.
def traduction(choix,plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu) :
		
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
	coordonnees = [ligne][colonne]
	return coordonnees

def verification_demande(choix,plateau,joueur,premier_joueur,symbole,tour,dejavu) :
		
	choix = 0
	while choix not in ('1','2','3','4','5','6','7','8','9') :
		afficher(plateau)
		choix = input("Choisissez un emplacement en écrivant le chiffre le représentant : ")
		print("")
	choix = int(choix)
	coordonnees = traduction(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	while estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,reponse,tour,dejavu) == False :
		verification_demande(choix,plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu)		
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix)
	return choix

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau,reponse) :
	
	afficher(plateau)
	if reponse == "N" :
		if joueur == "joueur" :
			joueur == "IA"
		else :
			joueur == "joueur"
	if joueur == "joueur" :
		print("Vous avez gagné")
	if joueur == "IA" :
		print("L'IA a gagné")
	print("")
	morpion()

#Affiche qu'il y a égalité.			
def egalite() :
	
	print("Il y a égalité.")
	print("")
	morpion()
	
def empecheVictoire(premier_joueur,symbole,choix,plateau) :
	
	if (premier_joueur == "joueur" and symbole == "O" or premier_joueur == "IA" and symbole == "O" or 
	premier_joueur == "joueur" and symbole == "X" or premier_joueur == "IA" and symbole == "X") :
		if choix == 1 :
			if (plateau[0][0] == 1 and plateau[0][1] == "O" and plateau[0][2] == "O" or	
			plateau[0][0] == 1 and plateau[1][0] == "O" and plateau[2][0] == "O" or
			plateau[0][0] == 1 and plateau[1][1] == "O" and plateau[2][2] == "O" or
			plateau[0][0] == 1 and plateau[0][1] == "X" and plateau[0][2] == "X" or
			plateau[0][0] == 1 and plateau[1][0] == "X" and plateau[2][0] == "X" or
			plateau[0][0] == 1 and plateau[1][1] == "X" and plateau[2][2] == "X") :
				return True
		if choix == 2 :
			if (plateau[0][0] == "O" and plateau[0][1] == 2 and plateau[0][2] == "O" or
			plateau[0][1] == 2 and plateau[1][1] == "O" and plateau[2][1] == "O" or
			plateau[0][0] == "X" and plateau[0][1] == 2 and plateau[0][2] == "X" or
			plateau[0][1] == 2 and plateau[1][1] == "X" and plateau[2][1] == "X") :
				return True
		if choix == 3 :
			if (plateau[0][0] == "O" and plateau[0][1] == "O" and plateau[0][2] == 3 or
			plateau[0][2] == 3 and plateau[1][2] == "O" and plateau[2][2] == "O" or	
			plateau[0][2] == 3 and plateau[1][1] == "O" and plateau[2][0] == "O" or
			plateau[0][0] == "X" and plateau[0][1] == "X" and plateau[0][2] == 3 or
			plateau[0][2] == 3 and plateau[1][2] == "X" and plateau[2][2] == "X" or
			plateau[0][2] == 3 and plateau[1][1] == "X" and plateau[2][0] == "X") :
				return True
		if choix == 4 :
			if (plateau[1][0] == 4 and plateau[1][1] == "O" and plateau[1][2] == "O" or
			plateau[0][0] == "O" and plateau[1][0] == 4 and plateau[2][0] == "O" or 
			plateau[1][0] == 4 and plateau[1][1] == "X" and plateau[1][2] == "X" or
			plateau[0][0] == "X" and plateau[1][0] == 4 and plateau[2][0] == "X") :
				return True
		if choix == 5 :
			if (plateau[1][0] == "O" and plateau[1][1] == 5 and plateau[1][2] == "O" or
			plateau[0][1] == "O" and plateau[1][1] == 5 and plateau[2][1] == "O" or
			plateau[0][0] == "O" and plateau[1][1] == 5 and plateau[2][2] == "O" or
			plateau[0][2] == "O" and plateau[1][1] == 5 and plateau[2][0] == "O" or 
			plateau[1][0] == "X" and plateau[1][1] == 5 and plateau[1][2] == "X" or	
			plateau[0][1] == "X" and plateau[1][1] == 5 and plateau[2][1] == "X" or
			plateau[0][0] == "X" and plateau[1][1] == 5 and plateau[2][2] == "X" or
			plateau[0][2] == "X" and plateau[1][1] == 5 and plateau[2][0] == "X") :
				return True
		if choix == 6 :
			if (plateau[1][0] == "O" and plateau[1][1] == "O" and plateau[1][2] == 6 or
			plateau[0][2] == "O" and plateau[1][2] == 6 and plateau[2][2] == "O" or 
			plateau[1][0] == "X" and plateau[1][1] == "X" and plateau[1][2] == 6 or
			plateau[0][2] == "X" and plateau[1][2] == 6 and plateau[2][2] == "X") :
				return True
		if choix == 7 :
			if (plateau[2][0] == 7 and plateau[2][1] == "O" and plateau[2][2] == "O" or
			plateau[0][0] == "O" and plateau[1][0] == "O" and plateau[2][0] == 7 or
			plateau[0][2] == "O" and plateau[1][1] == "O" and plateau[2][0] == 7 or
			plateau[2][0] == 7 and plateau[2][1] == "X" and plateau[2][2] == "X" or
			plateau[0][0] == "X" and plateau[1][0] == "X" and plateau[2][0] == 7 or
			plateau[0][2] == "X" and plateau[1][1] == "X" and plateau[2][0] == 7) :
				return True
		if choix == 8 :
			if (plateau[2][0] == "O" and plateau[2][1] == 8 and plateau[2][2] == "O" or
			plateau[0][1] == "O" and plateau[1][1] == "O" and plateau[2][1] == 8 or 
			plateau[2][0] == "X" and plateau[2][1] == 8 and plateau[2][2] == "X" or
			plateau[0][1] == "X" and plateau[1][1] == "X" and plateau[2][1] == 8) :
				return True
		if choix == 9 :
			if (plateau[2][0] == "O" and plateau[2][1] == "O" and plateau[2][2] == 9 or	
			plateau[0][2] == "O" and plateau[1][2] == "O" and plateau[2][2] == 9 or	
			plateau[0][0] == "O" and plateau[1][1] == "O" and plateau[2][2] == 9 or
			plateau[2][0] == "X" and plateau[2][1] == "X" and plateau[2][2] == 9 or
			plateau[0][2] == "X" and plateau[1][2] == "X" and plateau[2][2] == 9 or
			plateau[0][0] == "X" and plateau[1][1] == "X" and plateau[2][2] == 9) :
				return True

#Vérifie si il y a un gagnant et retourne True si c'est le cas.			
def estVictorieux(joueur,premier_joueur,symbole,plateau) :
		
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

#Compte le nombre de cases complétées et retourne True si il y en a 8.				
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(len(plateau)) :
		for j in range(len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 8 :
		return True		
		
def obligation(tour,dejavu,plateau,symbole,joueur,premier_joueur,reponse) :
	
	if plateau == [["X","X",3],["X","O","O"],[7,"O","O"]] or plateau == [["X",2,"X"],["X","O","O"],[7,"O","O"]] :
		plateau = [["X","X","X"],["X","O","O"],[7,"O","O"]]			
	if plateau == [["X","X",3],[4,"O","O"],["X","O","O"]] or plateau == [["X",2,"X"],[4,"O","O"],["X","O","O"]] :
		plateau = [["X","X","X"],[4,"O","O"],["X","O","O"]]										
	if plateau == [[1,"X","X"],["O","O","X"],["O","O",9]] or plateau == [["X",2,"X"],["O","O","X"],["O","O",9]] :
		plateau = [["X","X","X"],["O","O","X"],["O","O",9]]			
	if plateau == [[1,"X","X"],["O","O",6],["O","O","X"]] or plateau == [["X",2,"X"],["O","O",6],["O","O","X"]] :
		plateau = [["X","X","X"],["O","O",6],["O","O","X"]]									
	if plateau == [[1,"O","O"],["X","O","O"],["X","X",9]] or plateau == [[1,"O","O"],["X","O","O"],["X",8,"X"]] :
		plateau = [["X","O","O"],["X","O","O"],["X","X",9]]					
	if plateau == [["X","O","O"],[4,"O","O"],["X","X",9]] or plateau == [["X","O","O"],[4,"O","O"],["X",8,"X"]] :
		plateau = [["X","O","O"],[4,"O","O"],["X","X","X"]]										
	if plateau == [["O","O",3],["O","O","X"],[7,"X","X"]] or plateau == [["O","O",3],["O","O","X"],["X",8,"X"]] :
		plateau = [["O","O",3],["O","O","X"],["X","X","X"]]					
	if plateau == [["O","O","X"],["O","O",6],[7,"X","X"]] or plateau == [["O","O","X"],["O","O",6],["X",8,"X"]] :
		plateau = [["O","O","X"],["O","O",6],["X","X","X"]]
	if plateau == [["X","X",3],["O","X","O"],["O","O",9]] or plateau == [["X","X",3],["O",5,"O"],["O","O","X"]] :
		plateau = [["X","X",3],["O","X","O"],["O","O","X"]]					
	if plateau == [["X",2,"X"],["O","X","O"],["O","O",9]] or plateau == [["X",2,"X"],["O",5,"O"],["O","O","X"]] :
		plateau = [["X",2,"X"],["O","X","O"],["O","O","X"]]										
	if plateau == [[1,"X","X"],["O","X","O"],[7,"O","O"]] or plateau == [[1,"X","X"],["O",5,"O"],["X","O","O"]] :
		plateau = [[1,"X","X"],["O","X","O"],["X","O","O"]]					
	if plateau == [["X",2,"X"],["O","X","O"],[7,"O","O"]] or plateau == [["X",2,"X"],["O",5,"O"],["X","O","O"]] :
		plateau = [["X",2,"X"],["O","X","O"],["X","O","O"]]									
	if plateau == [["X","O","O"],["X","X","O"],[7,"O",9]] or plateau == [["X","O","O"],["X",5,"O"],[7,"O","X"]] :
		plateau = [["X","O","O"],["X","X","O"],[7,"O","X"]]					
	if plateau == [["X","O","O"],[4,"X","O"],["X","O",9]] or plateau == [["X","O","O"],[4,5,"O"],["X","O","X"]] :
		plateau = [["X","O","O"],[4,"X","O"],["X","O","X"]]									
	if plateau == [[1,"O",3],["X","X","O"],["X","O","O"]] or plateau == [[1,"O","X"],["X",5,"O"],["X","O","O"]] :
		plateau = [[1,"O","X"],["X","X","O"],["X","O","O"]]					
	if plateau == [["X","O",3],[4,"X","O"],["X","O","O"]] or plateau == [["X","O","X"],[4,5,"O"],["X","O","O"]] :
		plateau = [["X","O","X"],[4,"X","O"],["X","O","O"]]									
	if plateau == [["O","O",3],["O","X","O"],["X","X",9]] or plateau == [["O","O","X"],["O",5,"O"],["X","X",9]] :
		plateau = [["O","O","X"],["O","X","O"],["X","X",9]]					
	if plateau == [["O","O",3],["O","X","O"],["X",8,"X"]] or plateau == [["O","O","X"],["O",5,"O"],["X",8,"X"]] :
		plateau = [["O","O","X"],["O","X","O"],["X",8,"X"]]									
	if plateau == [[1,"O","O"],["O","X","O"],[7,"X","X"]] or plateau == [["X","O","O"],["O",5,"O"],[7,"X","X"]] :
		plateau = [["X","O","O"],["O","X","O"],[7,"X","X"]]				
	if plateau == [[1,"O","O"],["O","X","O"],["X",8,"X"]] or plateau == [["X","O","O"],["O",5,"O"],["X",8,"X"]] :
		plateau = [["X","O","O"],["O","X","O"],["X",8,"X"]]										
	if plateau == [[1,"O",3],["O","X","X"],["O","O","X"]] or plateau == [["X","O",3],["O",5,"X"],["O","O","X"]] :
		plateau = [["X","O",3],["O","X","X"],["O","O","X"]]					
	if plateau == [[1,"O","X"],["O","X",6],["O","O","X"]] or plateau == [["X","O","X"],["O",5,6],["O","O","X"]] :
		plateau = [["X","O","X"],["O","X",6],["O","O","X"]]					
	if plateau == [["O","O","X"],["O","X","X"],[7,"O",9]] or plateau == [["O","O","X"],["O",5,"X"],["X","O",9]] :
		plateau = [["O","O","X"],["O","X","X"],["X","O",9]]					
	if plateau == [["O","O","X"],["O","X",6],[7,"O","X"]] or plateau == [["O","O","X"],["O",5,6],["X","O","X"]] :
		plateau = [["O","O","X"],["O","X",6],["X","O","X"]]									
	if plateau == [["X","X",3],["O","X","O"],["O",8,"O"]] or plateau == [[1,"X","X"],["O","X","O"],["O",8,"O"]] :
		plateau = [["X","X","X"],["O","X","O"],["O",8,"O"]]					
	if plateau == [["X","X",3],["O",5,"O"],["O","X","O"]] or plateau == [[1,"X","X"],["O",5,"O"],["O","X","O"]] :
		plateau = [["X","X","X"],["O",5,"O"],["O","X","O"]]										
	if plateau == [["X","O","O"],["X","X",6],[7,"O","O"]] or plateau == [[1,"O","O"],["X","X",6],["X","O","O"]] :
		plateau = [["X","O","O"],["X","X",6],["X","O","O"]]					
	if plateau == [["X","O","O"],["X",5,"X"],[7,"O","O"]] or plateau == [[1,"O","O"],["X",5,"X"],["X","O","O"]] :
		plateau = [["X","O","O"],["X",5,"X"],["X","O","O"]]									
	if plateau == [["O",2,"O"],["O","X","O"],["X","X",9]] or plateau == [["O",2,"O"],["O","X","O"],[7,"X","X"]] :
		plateau = [["O",2,"O"],["O","X","O"],["X","X","X"]]					
	if plateau == [["O","X","O"],["O",5,"O"],["X","X",9]] or plateau == [["O","X","O"],["O",5,"O"],[7,"X","X"]] :
		plateau = [["O","X","O"],["O",5,"O"],["X","X","X"]]										
	if plateau == [["O","O","X"],[4,"X","X"],["O","O",9]] or plateau == [["O","O",3],[4,"X","X"],["O","O","X"]] :
		plateau = [["O","O","X"],["X","X","X"],["O","O",9]]					
	if plateau == [["O","O","X"],["X",5,"X"],["O","O",9]] or plateau == [["O","O",3],["X",5,"X"],["O","O","X"]] :
		plateau = [["O","O","X"],["X","X","X"],["X","O",9]]													
	if plateau == [["X","O","X"],["O","X","O"],[7,"O",9]] :
		plateau = [["X","O","X"],["O","X","O"],["X","O",9]]					
	if plateau == [["X",2,"X"],["O","X","O"],["O","O",9]] :
		plateau = [["X","X","X"],["O","X","O"],["O","O",9]]					
	if plateau == [["X",2,"X"],["O","X","O"],[7,"O","O"]] :
		plateau = [["X","X","X"],["O","X","O"],[7,"O","O"]]									
	if plateau == [["X","O",3],["O","X","O"],["X","O",9]] :
		plateau = [["X","O","X"],["O","X","O"],["X","O",9]]					
	if plateau == [["X","O","O"],[4,"X","O"],["X","O",9]] :
		plateau = [["X","O","O"],["X","X","O"],["X","O",9]]					
	if plateau == [["X","O",3],[4,"X","O"],["X","O","O"]] :
		plateau = [["X","O","X"],[4,"X","O"],["X","O","O"]]										
	if plateau == [[1,"O",3],["O","X","O"],["X","O","X"]] :
		plateau = [["X","O",3],["O","X","O"],["X","O","X"]]					
	if plateau == [["O","O",3],["O","X","O"],["X",8,"X"]] :
		plateau = [["O","O","X"],["O","X","O"],["X",8,"X"]]				
	if plateau == [[1,"O","O"],["O","X","O"],["X",8,"X"]] :
		plateau = [["X","O","O"],["O","X","O"],["X",8,"X"]]										
	if plateau == [[1,"O","X"],["O","X","O"],[7,"O","X"]] :
		plateau = [["X","O","X"],["O","X","O"],[7,"O","X"]]					
	if plateau == [["O","O","X"],["O","X","X"],[7,"O","X"]] :
		plateau = [["O","O","X"],["O","X","X"],[7,"O","X"]]					
	if plateau == [[1,"O","X"],["O","X",6],["O","O","X"]] :
		plateau = [[1,"O","X"],["O","X",6],["O","O","X"]]									
	if plateau == [["X","O","X"],[4,5,"O"],["X","O","O"]] :
		plateau == [["X","O","X"],[4,"X","O"],["X","O","O"]]				
	if plateau == [["X",2,"X"],["O",5,"O"],["X","O","O"]] :
		plateau == [["X",2,"X"],["O","X","O"],["X","O","O"]]										
	if plateau == [["X","O","X"],["O",5,6],["O","O","X"]] :
		plateau == [["X","O","X"],["O","X",6],["O","O","X"]]					
	if plateau == [["X",2,"X"],["O",5,"O"],["O","O","X"]] :
		plateau == [["X",2,"X"],["O","X","O"],["O","O","X"]]					
	if plateau == [["X","O","O"],["O",5,"O"],["X",8,"X"]] :
		plateau == [["X","O","O"],["O","X","O"],["X",8,"X"]]					
	if plateau == [["X","O","O"],[4,5,"O"],["X","O","X"]] :
		plateau == [["X","O","O"],[4,"X","O"],["X","O","X"]]			
	if plateau == [["O","O","X"],["O",5,"O"],["X",8,"X"]] :
		plateau == [["O","O","X"],["O","X","O"],["X",8,"X"]]					
	if plateau == [["O","O","X"],["O",5,6],["X","O","X"]] :
		plateau == [["O","O","X"],["O","X",6],["X","O","X"]]												
	if plateau == [["O","O",3],["O","X","X"],[7,"X","X"]] or plateau == [["O",2,"O"],["O","X","X"],[7,"X","X"]] :
		plateau = [["O","O","O"],["O","X","X"],[7,"X","X"]]			
	if plateau == [["O","O",3],[4,"X","X"],["O","X","X"]] or plateau == [["O",2,"O"],[4,"X","X"],["O","X","X"]] :
		plateau = [["O","O","O"],[4,"X","X"],["O","X","X"]]										
	if plateau == [[1,"O","O"],["X","X","O"],["X","X",9]] or plateau == [["O",2,"O"],["X","X","O"],["X","X",9]] :
		plateau = [["O","O","O"],["X","X","O"],["X","X",9]]				
	if plateau == [[1,"O","O"],["X","X",6],["X","X","O"]] or plateau == [["O",2,"O"],["X","X",6],["X","X","O"]] :
		plateau = [["O","O","O"],["X","X",6],["X","X","O"]]									
	if plateau == [[1,"X","X"],["O","X","X"],["O","O",9]] or plateau == [[1,"X","X"],["O","X","X"],["O",8,"O"]] :
		plateau = [["O","X","X"],["O","X","X"],["O","O",9]]					
	if plateau == [["O","X","X"],[4,"X","X"],["O","O",9]] or plateau == [["O","X","X"],[4,"X","X"],["O",8,"O"]] :
		plateau = [["O","X","X"],[4,"X","X"],["O","O","O"]]				
	if plateau == [["X","X",3],["X","X","O"],[7,"O","O"]] or plateau == [["X","X",3],["X","X","O"],["O",8,"O"]] :
		plateau = [["X","X",3],["X","X","O"],["O","O","O"]]					
	if plateau == [["X","X","O"],["X","X",6],[7,"O","O"]] or plateau == [["X","X","O"],["X","X",6],["O",8,"O"]] :
		plateau = [["X","X","O"],["X","X",6],["O","O","O"]]
	if plateau == [["O","O",3],["X","O","X"],["X","X",9]] or plateau == [["O","O",3],["X",5,"X"],["X","X","O"]] :
		plateau = [["O","O",3],["X","O","X"],["X","X","O"]]					
	if plateau == [["O",2,"O"],["X","O","X"],["X","X",9]] or plateau == [["O",2,"O"],["X",5,"X"],["X","X","O"]] :
		plateau = [["O",2,"O"],["X","O","X"],["X","X","O"]]										
	if plateau == [[1,"O","O"],["X","O","X"],[7,"X","X"]] or plateau == [[1,"O","O"],["X",5,"X"],["O","X","X"]] :
		plateau = [[1,"O","O"],["X","O","X"],["O","X","X"]]					
	if plateau == [["O",2,"O"],["X","O","X"],[7,"X","X"]] or plateau == [["O",2,"O"],["X",5,"X"],["O","X","X"]] :
		plateau = [["O",2,"O"],["X","O","X"],["O","X","X"]]									
	if plateau == [["O","X","X"],["O","O","X"],[7,"X",9]] or plateau == [["O","X","X"],["O",5,"X"],[7,"X","O"]] :
		plateau = [["O","X","X"],["O","O","X"],[7,"X","O"]]					
	if plateau == [["O","X","X"],[4,"O","X"],["O","X",9]] or plateau == [["O","X","X"],[4,5,"X"],["O","X","O"]] :
		plateau = [["O","X","X"],[4,"O","X"],["O","X","O"]]									
	if plateau == [[1,"X",3],["O","O","X"],["O","X","X"]] or plateau == [[1,"X","O"],["O",5,"X"],["O","X","X"]] :
		plateau = [[1,"X","O"],["O","O","X"],["O","X","X"]]					
	if plateau == [["O","X",3],[4,"O","X"],["O","X","X"]] or plateau == [["O","X","O"],[4,5,"X"],["O","X","X"]] :
		plateau = [["O","X","O"],[4,"O","X"],["O","X","X"]]									
	if plateau == [["X","X",3],["X","O","X"],["O","O",9]] or plateau == [["X","X","O"],["X",5,"X"],["O","O",9]] :
		plateau = [["X","X","O"],["X","O","X"],["O","O",9]]					
	if plateau == [["X","X",3],["X","O","X"],["O",8,"O"]] or plateau == [["X","X","O"],["X",5,"X"],["O",8,"O"]] :
		plateau = [["X","X","O"],["X","O","X"],["O",8,"O"]]										
	if plateau == [[1,"X","X"],["X","O","X"],[7,"O","O"]] or plateau == [["O","X","X"],["X",5,"X"],[7,"O","O"]] :
		plateau = [["O","X","X"],["X","O","X"],[7,"O","O"]]					
	if plateau == [[1,"X","X"],["X","O","X"],["O",8,"O"]] or plateau == [["O","X","X"],["X",5,"X"],["O",8,"O"]] :
		plateau = [["O","X","X"],["X","O","X"],["O",8,"O"]]										
	if plateau == [[1,"X",3],["X","O","O"],["X","X","O"]] or plateau == [["O","X",3],["X",5,"O"],["X","X","O"]] :
		plateau = [["O","X",3],["X","O","O"],["X","X","O"]]					
	if plateau == [[1,"X","O"],["X","O",6],["X","X","O"]] or plateau == [["O","X","O"],["X",5,6],["X","X","O"]] :
		plateau = [["O","X","O"],["X","O",6],["X","X","O"]]				
	if plateau == [["X","X","O"],["X","O","O"],[7,"X",9]] or plateau == [["X","X","O"],["X",5,"O"],["O","X",9]] :
		plateau = [["X","X","O"],["X","O","O"],["O","X",9]]					
	if plateau == [["X","X","O"],["X","O",6],[7,"X","O"]] or plateau == [["X","X","O"],["X",5,6],["O","X","O"]] :
		plateau = [["X","X","O"],["X","O",6],["O","X","O"]]								
	if plateau == [["O","O",3],["X","O","X"],["X",8,"X"]] or plateau == [[1,"O","O"],["X","O","X"],["X",8,"X"]] :
		plateau = [["O","O","O"],["X","O","X"],["X",8,"X"]]					
	if plateau == [["O","O",3],["X",5,"X"],["X","O","X"]] or plateau == [[1,"O","O"],["X",5,"X"],["X","O","X"]] :
		plateau = [["O","O","O"],["X",5,"X"],["X","O","X"]]									
	if plateau == [["O","X","X"],["O","O",6],[7,"X","X"]] or plateau == [[1,"X","X"],["O","O",6],["O","X","X"]] :
		plateau = [["O","X","X"],["O","O",6],["O","X","X"]]			
	if plateau == [["O","X","X"],["O",5,"O"],[7,"X","X"]] or plateau == [[1,"X","X"],["O",5,"O"],["O","X","X"]] :
		plateau = [["O","X","X"],["O",5,"O"],["O","X","X"]]									
	if plateau == [["X",2,"X"],["X","O","X"],["O","O",9]] or plateau == [["X",2,"X"],["X","O","X"],[7,"O","O"]] :
		plateau = [["X",2,"X"],["X","O","X"],["O","O","O"]]					
	if plateau == [["X","O","X"],["X",5,"X"],["O","O",9]] or plateau == [["X","O","X"],["X",5,"X"],[7,"O","O"]] :
		plateau = [["X","O","X"],["X",5,"X"],["O","O","O"]]				
	if plateau == [["X","X","O"],[4,"O","O"],["X","X",9]] or plateau == [["X","X",3],[4,"O","O"],["X","X","O"]] :
		plateau = [["X","X","O"],["O","O","O"],["X","X",9]]					
	if plateau == [["X","X","O"],["O",5,"O"],["X","X",9]] or plateau == [["X","X",3],["O",5,"O"],["X","X","O"]] :
		plateau = [["X","X","O"],["O","O","O"],["O","X",9]]									
	if plateau == [["O","X","O"],["X","O","X"],[7,"X",9]] :
		plateau = [["O","X","O"],["X","O","X"],["O","X",9]]					
	if plateau == [["O",2,"O"],["X","O","X"],["X","X",9]] :
		plateau = [["O","O","O"],["X","O","X"],["X","X",9]]					
	if plateau == [["O",2,"O"],["X","O","X"],[7,"X","X"]] :
		plateau = [["O","O","O"],["X","O","X"],[7,"X","X"]]									
	if plateau == [["O","X",3],["X","O","X"],["O","X",9]] :
		plateau = [["O","X","O"],["X","O","X"],["O","X",9]]					
	if plateau == [["O","X","X"],[4,"O","X"],["O","X",9]] :
		plateau = [["O","X","X"],["O","O","X"],["O","X",9]]					
	if plateau == [["O","X",3],[4,"O","X"],["O","X","X"]] :
		plateau = [["O","X","O"],[4,"O","X"],["O","X","X"]]										
	if plateau == [[1,"X",3],["X","O","X"],["O","X","O"]] :
		plateau = [["O","X",3],["X","O","X"],["O","X","O"]]					
	if plateau == [["X","X",3],["X","O","X"],["O",8,"O"]] :
		plateau = [["X","X","O"],["X","O","X"],["O",8,"O"]]					
	if plateau == [[1,"X","X"],["X","O","X"],["O",8,"O"]] :
		plateau = [["O","X","X"],["X","O","X"],["O",8,"O"]]										
	if plateau == [[1,"X","O"],["X","O","X"],[7,"X","O"]] :
		plateau = [["O","X","O"],["X","O","X"],[7,"X","O"]]					
	if plateau == [["X","X","O"],["X","O","O"],[7,"X","O"]] :
		plateau = [["X","X","O"],["X","O","O"],[7,"X","O"]]					
	if plateau == [[1,"X","O"],["X","O",6],["X","X","O"]] :
		plateau = [[1,"X","O"],["X","O",6],["X","X","O"]]		
	if plateau == [["O","X","O"],[4,5,"X"],["O","X","X"]] :
		plateau == [["O","X","O"],[4,"O","X"],["O","X","X"]]				
	if plateau == [["O",2,"O"],["X",5,"X"],["O","X","X"]] :
		plateau == [["O",2,"O"],["X","O","X"],["O","X","X"]]										
	if plateau == [["O","X","O"],["X",5,6],["X","X","O"]] :
		plateau == [["O","X","O"],["X","O",6],["X","X","O"]]					
	if plateau == [["O",2,"O"],["X",5,"X"],["X","X","O"]] :
		plateau == [["O",2,"O"],["X","O","X"],["X","X","O"]]					
	if plateau == [["O","X","X"],["X",5,"X"],["O",8,"O"]] :
		plateau == [["O","X","X"],["X","O","X"],["O",8,"O"]]					
	if plateau == [["O","X","X"],[4,5,"X"],["O","X","O"]] :
		plateau == [["O","X","X"],[4,"O","X"],["O","X","O"]]				
	if plateau == [["X","X","O"],["X",5,"X"],["O",8,"O"]] :
		plateau == [["X","X","O"],["X","O","X"],["O",8,"O"]]				
	if plateau == [["X","X","O"],["X",5,6],["O","X","O"]] :
		plateau == [["X","X","O"],["X","O",6],["O","X","O"]]
	essais = 0
	if tour == 8 :
		while essais < 4 :
			choix = remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
			if estVictorieux(joueur,premier_joueur,symbole,plateau) == True :
				essais += 1
				coordonnees = traduction(choix)
				ligne = coordonnees[0]
				colonne = coordonnees[1]
				enlever(plateau,ligne,colonne,choix)
				if essais == 2 and tour == 8 or essais == 3 and tour == 7 :
					dejavu = []
					remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
					break
			else :
				break
		if estVictorieux(joueur,premier_joueur,symbole,plateau) == True :	
			victoire(joueur,plateau,reponse)
		else :
			print("L'IA a les croix") 
			tour = 9
			joueur = "joueur"
			remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau)
			if estVictorieux(joueur,premier_joueur,symbole,plateau) == True :
				victoire(joueur,plateau,reponse)
			egalite()
	
	return plateau	

def decision(plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu) :
	 
	erreur = 1
	joueur = "IA"
	choix = randint(1,9)
	coordonnees = traduction(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	while erreur == 1 :
		if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix,reponse,tour,dejavu) == False :
			choix = randint(1,9)
			coordonnees = traduction(choix)
			ligne = coordonnees[0]
			colonne = coordonnees[1]
		else :
			break				
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix)
	return choix 

#Utilise la méthode "traduction_choix" pour avoir la ligne et la colonne du choix à enlever du plateau.
def enlever(plateau,ligne,colonne,choix) :
		
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix

def remplir(tour,dejavu,joueur,premier_joueur,symbole,plateau) :
	
	choix = 0
	if tour == 8 :		
		if (joueur == "IA" and premier_joueur == "joueur" and symbole == "X" or
		joueur == "IA" and premier_joueur == "IA" and symbole == "X") :
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
		if (joueur == "IA" and premier_joueur == "joueur" and symbole == "O" or
		joueur == "IA" and premier_joueur == "IA" and symbole == "O") :				
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
	if tour == 9 :		
		if aLesRonds(joueur,premier_joueur,symbole) == True :				
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
		else :			
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
		print("Remplissage de la dernière case disponible")
		print("")
		afficher(plateau)
	afficher(plateau)
	return choix
	
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
	dejavu = []
	premier_joueur = "joueur"
	joueur = "joueur"
	reponse = "a"
	symbole = "a"
	tour = 1
	print("IA morpion perdante")
	print("")
	while not reponse == "O" and reponse != "N" or not reponse != "O" and reponse == "N" :
		reponse = input("Appuyez sur O puis Entrée si vous voulez commencer ou N puis Entrée si vous ne voulez pas : ")
		print("")
	while not symbole == "O" and symbole != "X" or not symbole != "O" and symbole == "X" :
		symbole = input("Appuyez sur O si vous voulez les O ou X puis Entrée si vous voulez les X : ")
		print("")
	if reponse == "N" :
		premier_joueur = "IA"
	while estVictorieux(joueur,premier_joueur,symbole,plateau) != True :
		if reponse == "N" :
			plateau = decision(plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu)
			tour += 1
		choix = verification_demande(choix,plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu)
		tour += 1
		if reponse == "O" :
			plateau = decision(plateau,joueur,premier_joueur,symbole,reponse,tour,dejavu)
			tour += 1
				
morpion()		
