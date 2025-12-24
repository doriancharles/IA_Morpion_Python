from random import randint

plateau = [[1,2,3],[4,5,6],[7,8,9]]
choix = 0

def afficher(plateau) :
		
	for i in range(0,len(plateau)) :
		print(plateau[i])
	print("")
		
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne) :
	
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "O" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "X") :
		plateau[ligne][colonne] = "O"
	
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "X" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "O") :
		plateau[ligne][colonne] = "X"
	
	if joueur == "IA" :
		localisation(ligne,colonne)
		
	if joueur == "joueur" :
		print("Vous avez les ",symbole)
		print("")
		afficher(plateau)
	return plateau
	
def estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix) :
		
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
		if empecheVictoire(premier_joueur,symbole,choix,plateau) == True :
			return False
	else :
		return True
			
def verification(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix) :
	
	while estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix) == False :
		verification_demande(choix,plateau,joueur,premier_joueur,symbole)		
	return plateau
	return choix
	
def traduction(choix,plateau,joueur,premier_joueur,symbole) :
		
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
		
	verification(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix)
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne)
	return ligne
	return colonne	
	return choix
	return plateau	

def verification_demande(choix,plateau,joueur,premier_joueur,symbole) :
		
	choix = 0
	while choix not in ('1','2','3','4','5','6','7','8','9') :
		afficher(plateau)
		choix = input("Choisissez un emplacement en écrivant le chiffre le représentant : ")
		print("")
	choix = int(choix)
	traduction(choix,plateau,joueur,premier_joueur,symbole)
	return choix
	return plateau
		
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
			
def egalite() :
	
	print("Il y a égalité.")
	print("")
	morpion()
	
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
		
		
def estEgalitaire(plateau) :
	
	compte = 0
	total = 0
	for i in range(0,len(plateau)) :
		for j in range(0,len(plateau)) :
			if plateau[i][j] == "X" or plateau[i][j] == "O" :
				total += 1
	if total == 8 :
		return True			

def decision(plateau,joueur,premier_joueur,symbole,reponse) :
	 
	erreur = 1
	joueur = "IA"
	choix = randint(1,9)
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
	while erreur == 1 :
		if estPossible(plateau,joueur,premier_joueur,symbole,ligne,colonne,choix) == False :
			choix = randint(1,9)
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
		else :
			break	
			
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne)
	if estVictorieux(plateau) == True :
			victoire(joueur,plateau,reponse)
	if estEgalitaire(plateau) == True :
		remplir(plateau,symbole,joueur,premier_joueur)
		if estVictorieux(plateau) == True :
			joueur = changer(joueur)
			victoire(joueur,plateau,reponse)
		egalite()
	
	return plateau
	return choix 

def enlever(plateau,ligne,colonne,choix) :
	
	if plateau[ligne][colonne] == "O" or plateau[ligne][colonne] == "X" :
		plateau[ligne][colonne] = choix

def remplir(plateau,symbole,joueur,premier_joueur) :
	
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "X" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "O") :
		
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
			
	if (joueur == "joueur" and premier_joueur == "joueur" and symbole == "O" or
	joueur == "joueur" and premier_joueur == "IA" and symbole == "O" or
	joueur == "IA" and premier_joueur == "joueur" and symbole == "X" or
	joueur == "IA" and premier_joueur == "IA" and symbole == "X") :
		
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
	
def localisation(ligne,colonne) :
	
	if ligne == 0 :
		if colonne == 0 :
			choix = 1
		if colonne == 1 :
			choix = 2
		if colonne == 2 :
			choix = 3
			
	if ligne == 1 :
		if colonne == 0 :
			choix = 4
		if colonne == 1 :
			choix = 5
		if colonne == 2 :
			choix = 6
			
	if ligne == 2 :
		if colonne == 0 :
			choix = 7
		if colonne == 1 :
			choix = 8
		if colonne == 2 :
			choix = 9
			
	print("L'IA a joué ",choix)
	print("")
	
def changer(joueur) :
	
	if joueur == "IA" :
		joueur = "joueur"
	else :
		joueur = "IA" 
	return joueur

def inverser(symbole) :
	
	if symbole == "O" :
		symbole = "X"
	else :
		symbole = "IA" 
	return symbole

def morpion() :
	
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	premier_joueur = "joueur"
	joueur = "joueur"
	reponse = "a"
	symbole = "a"
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
	choix = verification_demande(choix,plateau,joueur,premier_joueur,symbole)	
	while estVictorieux(plateau) != True :
		if reponse == "N" :
			plateau = decision(plateau,joueur,premier_joueur,symbole,reponse)
		choix = verification_demande(choix,plateau,joueur,premier_joueur,symbole)
		if estVictorieux(plateau) == True :
			victoire(joueur,plateau,reponse)
		if estEgalitaire(plateau) == True :
			remplir(plateau,symbole,joueur,premier_joueur)
			if estVictorieux(plateau) == True :
				joueur = changer(joueur)
				victoire(joueur,plateau,reponse)
			egalite()
		if reponse == "O" :
			plateau = decision(plateau,joueur,premier_joueur,symbole,reponse)
				
morpion()		


