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
	if joueur == "joueur" :
		print("Vous avez les ",symbole)
		print("")
	afficher(plateau)
	if estVictorieux(plateau) == True :
		victoire(joueur,plateau)
	if estEgalitaire(plateau) == True :
		joueur = remplir(plateau,symbole,joueur,premier_joueur)
		if estVictorieux(plateau) == True :
			victoire(joueur,plateau)
		egalite()

#Vérifie si il y a déjà un symbole à l'endroit choisi par le joueur, retourne False si c'est le cas et affiche un message d'erreur en fonction d'à qui il appartient.
def estPossible(joueur,plateau,symbole,ligne,colonne) :

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
		print("")
	else :
		print("L'IA joue la dernière case")
		print("")
	afficher(plateau)
	return joueur

def verification_demande(choix,plateau,joueur,symbole,premier_joueur) :

	choix = 0
	while choix not in ('1','2','3','4','5','6','7','8','9') :
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
	if estPossible(joueur,plateau,symbole,ligne,colonne) == False :
		verification_demande(choix,plateau,joueur,symbole,premier_joueur)
	else :
		placer_valeur(joueur,premier_joueur,symbole,plateau,ligne,colonne,choix) 
	return choix

#Affiche le gagnant en l'informant de sa victoire.
def victoire() :

	print("L'IA a gagné")
	print("")
	morpion()

#Affiche qu'il y a égalité.
def egalite() :

	print("Il y a égalité.")
	print("")
	morpion()

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
	print("IA morpion imbattable rapide")
	print("")
	while not reponse == "O" and reponse != "N" or not reponse != "O" and reponse == "N" :
		reponse = input("Appuyez sur O puis Entrée si vous voulez commencer ou N puis Entrée si vous ne voulez pas : ")
		print("")
	while not symbole == "O" and symbole != "X" or not symbole != "O" and symbole == "X" :
		symbole = input("Appuyez sur O si vous voulez les O ou X puis Entrée si vous voulez les X : ")
		print("")
	if reponse == "O" :
		choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
		if choix == 1 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
		if choix == 2 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 8 :
				print("Vous avez déjà perdu")
				print("")
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
		if choix == 3 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 1 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
		if choix == 4 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)

					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)

					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 6 :
				print("Vous avez déjà perdu")
				print("")
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)					 
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
		if choix == 5 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					print("Vous avez déjà perdu")
					print("")
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)

					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)

					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
				if choix == 7 :
					print("Vous avez déjà perdu")
					print("")
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 6 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 1 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			if choix == 4 :
				print("Vous avez déjà perdu")
				print("")
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
		if choix == 7 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 1 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 8 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,2,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
			if choix == 2 :
				print("Vous avez déjà perdu")
				print("")
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,2,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 1 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 1 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)								 
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
		if choix == 9 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 1 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			if choix == 3 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 8 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)								 
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 8 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 3 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
			if choix == 6 :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 2 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,1,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			if choix == 7 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 2 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,0,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
			if choix == 8 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
						placer_valeur("joueur",premier_joueur,symbole,plateau,0,1,choix)
					else :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
	if reponse == "N" :
		premier_joueur = "IA"
		placer_valeur("IA",premier_joueur,symbole,plateau,0,0,choix)
		choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
		if choix == 2 :
			placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 9 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
		if choix == 3 :
			placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 5 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
		if choix == 4 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 5 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				if choix == 6 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)

					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 4 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
					if choix == 9 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
				if choix == 9 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
					choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
					if choix == 6 :
						placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
					if choix == 7 :
						placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 6 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 7 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 7 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				if choix == 5 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)
		if choix == 8 :
			placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 4 :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 3 :
					placer_valeur("IA",premier_joueur,symbole,plateau,2,2,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
		if choix == 9 :
			placer_valeur("IA",premier_joueur,symbole,plateau,0,2,choix)
			choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
			if choix == 2 :
				placer_valeur("IA",premier_joueur,symbole,plateau,2,0,choix)
				choix = verification_demande(choix,plateau,joueur,symbole,premier_joueur)
				if choix == 4 :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,1,choix)
				else :
					placer_valeur("IA",premier_joueur,symbole,plateau,1,0,choix)
			else :
				placer_valeur("IA",premier_joueur,symbole,plateau,0,1,choix)

morpion()
