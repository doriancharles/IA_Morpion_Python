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
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant) :
	
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"
	else :
		plateau[ligne][colonne] = "X"
	if joueur == "IA" :
		print("L'IA a joué ",choix)
		print("")
	if joueur == "joueur" :
		print("Vous avez les ",symbole)
		print("")
	if estVictorieux(plateau) == True :		
		victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)	
	if estEgalitaire(plateau) == True :		
		if estVictorieux(plateau) == True :			
			joueur = changer(joueur)
			victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)			
		egalite(liste_Coups,liste_Coups_Gagnant)		
	afficher(plateau)
	
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
	
def verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant) :
			
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
		placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant) 
	return choix

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant) :
		
	afficher(plateau)		
	if joueur == "joueur" :	
		print("Vous avez gagné")	
		liste_Coups.append(choix)
		choix_change = liste_Coups[len(liste_Coups)-1]
		liste_Coups.pop()
		liste_Coups[len(liste_Coups)-1] = choix_change
		liste_Coups_Gagnant.append(liste_Coups)	
	else :				
		print("L'IA a gagné")			
	print("")
	morpion(liste_Coups_Gagnant)			

#Affiche qu'il y a égalité.			
def egalite(liste_Coups_Gagnant) :
		
	afficher(plateau)
	print("Il y a égalité.")
	print("")
	morpion(liste_Coups_Gagnant)	

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

def decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant) :
	
	changement = 0
	joueur = "IA"
	if liste_Coups_Gagnant != [] :
		for i in range (len(liste_Coups_Gagnant)) :
			liste_Test = liste_Coups_Gagnant[i]
			print(liste_Test)
			choix = liste_Test[len(liste_Test)-1]
			print(choix)
			liste_Test.pop()
			print(liste_Test)
			if liste_Coups == liste_Test :
				changement = 1
			liste_Test.append(choix)
			if changement == 1 :
				break
	if changement != 1 :
		choix = remplir(plateau,symbole,joueur,premier_joueur)
	liste_Coups.append(choix)
	coordonnees = traduction(choix)
	ligne = coordonnees[0]
	colonne = coordonnees[1]
	placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix,liste_Coups,liste_Coups_Gagnant)
	if estVictorieux(plateau) == True :
		victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)	
	if estEgalitaire(plateau) == True :
		if estVictorieux(plateau) == True :
			joueur = changer(joueur)
			victoire(joueur,plateau,choix,liste_Coups,liste_Coups_Gagnant)
		egalite(liste_Coups,liste_Coups_Gagnant) 

def remplir(plateau,symbole,joueur,premier_joueur) :
	
	choix = 0
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		while choix == 0 :
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
		while choix == 0 :
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

def morpion(liste_Coups_Gagnant) :
		
	liste_Coups = []
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	premier_joueur = "joueur"
	joueur = "joueur"
	reponse = "a"
	symbole = "a"
	print("IA Machine Learning")
	print("")
	while not reponse == "O" and reponse != "N" or not reponse != "O" and reponse == "N" :
		reponse = input("Appuyez sur O puis Entrée si vous voulez commencer ou N puis Entrée si vous ne voulez pas : ")
		print("")
	while not symbole == "O" and symbole != "X" or not symbole != "O" and symbole == "X" :
		symbole = input("Appuyez sur O si vous voulez les O ou X puis Entrée si vous voulez les X : ")
		print("")
	if reponse == "N" :
		premier_joueur = "IA"
	if premier_joueur == "joueur" :			
		choix1 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix1)
		choix2 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix3 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix3)			
		choix4 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix5 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix5)					
		choix6 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix7 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix7)			
		choix8 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix9 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
	if premier_joueur == "IA" :		
		choix1 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix2 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix2)			
		choix3 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix4 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix4)
		choix5 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix6 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix6)			
		choix7 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		choix8 = verification_demande(joueur,plateau,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)
		liste_Coups.append(choix8)	
		choix9 = decision(plateau,joueur,premier_joueur,symbole,liste_Coups,liste_Coups_Gagnant)

liste_Coups_Gagnant = []					
morpion(liste_Coups_Gagnant)		

