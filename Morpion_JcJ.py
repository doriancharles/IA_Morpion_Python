#Affiche les 3 valeurs de chaque lignes, dans l'ordre, lignes par lignes.
def afficher(plateau) :
	
	for i in range(0,len(plateau)) :		
		print(plateau[i])	
	print ("")

#Vérifie que le joueur actuel a les ronds et retourne True si c'est le cas.	
def aLesRonds(joueur,premier_joueur,symbole) :
	
	if (joueur == "joueur 1" and premier_joueur == "joueur 1" and symbole == "O" or
	joueur == "joueur 1" and premier_joueur == "joueur 2" and symbole == "O" or
	joueur == "joueur 2" and premier_joueur == "joueur 1" and symbole == "X" or
	joueur == "joueur 2" and premier_joueur == "joueur 2" and symbole == "X") :			
		return True

#Met le symbole du joueur actuel à une place correspondante à un choix valide puis vérifie si il a gagné ou si il y a égalité.		
def placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne) :
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		plateau[ligne][colonne] = "O"		
	else :		
		plateau[ligne][colonne] = "X"	
	if estVictorieux(plateau) == True :
		victoire(joueur,plateau)
	if estEgalitaire(plateau) == True :
		remplir(plateau,symbole,joueur,premier_joueur)
		if estVictorieux(plateau) == True :
			joueur = changer(joueur)
			victoire(joueur,plateau)
		egalite()

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.					
def estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne) :
	if aLesRonds(joueur,premier_joueur,symbole) == True :
		if plateau[ligne][colonne] == "O" :
			print("Vous avez déjà choisi cette case")
			print("")
			return False
		if plateau[ligne][colonne] == "X" :
			print("Votre adversaire a déjà choisi cette case")
			print("")
			return False
	else :
		if plateau[ligne][colonne] == "X" :
			print("Case déjà choisie par vous")
			print("")
			return False	 
		if plateau[ligne][colonne] == "O" :							
			print("Votre adversaire a déjà choisi cette case")
			print("")
			return False
			
def verification_demande(joueur,plateau,premier_joueur,symbole) :
	
	choix = 0
	while choix not in ("1","2","3","4","5","6","7","8","9") :
		annoncer_tour(joueur)
		afficher(plateau)
		choix = input("Choisissez un emplacement en écrivant le chiffre le représentant : ")
		print("")
	choix = int(choix)	
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
	if estPossible(joueur,premier_joueur,symbole,plateau,ligne,colonne) == False :
		verification_demande(joueur,plateau,premier_joueur,symbole)
	else :
		placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne) 

#Affiche le gagnant en l'informant de sa victoire.		
def victoire(joueur,plateau) :
	
	afficher(plateau)
	print("Le " , joueur , " a gagné")
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

#Change la valeur de joueur passant de "joueur" en "IA"	ou l'inverse et la retourne.
def changer(joueur) :

	if joueur == "joueur 1" :
		joueur = "joueur 2"
	else :
		joueur = "joueur 1" 
	return joueur

	
def annoncer_tour(joueur) :
	print("Au tour du",joueur)
	print("")

def morpion() :
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	premier_joueur = "joueur 1"
	joueur = "joueur 1"
	reponse = "a"
	symbole = "a"
	print("Morpion JcJ")
	print("")
	while not reponse == "O" and reponse != "N" or not reponse != "O" and reponse == "N" :
		reponse = input("Appuyez sur O puis Entrée si vous voulez commencer ou N puis Entrée si vous ne voulez pas, joueur 1 : ")
	print("")
	while not symbole == "O" and symbole != "X" or not symbole != "O" and symbole == "X" :
		symbole = input("Appuyez sur O si vous voulez les O ou X puis Entrée si vous voulez les X, joueur 1 : ")
	print("")
	if reponse == "N" :
		premier_joueur = "joueur 2"
		joueur = "joueur 2"
	while estVictorieux(plateau) != True :
		verification_demande(joueur,plateau,premier_joueur,symbole)
		joueur = changer(joueur)
			
morpion()
