plateau = [[1,2,3],[4,5,6],[7,8,9]]
choix = 0

def afficher_plateau(plateau) :
		
	for i in range(0,len(plateau)) :
		print(plateau[i])
		
def placer_valeur(joueur,ligne,colonne,plateau) :
		
	if ligne == 0 :
		if colonne == 0 :
			if joueur == "IA" :
				plateau[0][0] = "X"
			if joueur == "joueur" :
				plateau[0][0] = "O"
		if colonne == 1 :
			if joueur == "IA" :
				plateau[0][1] = "X"
			if joueur == "joueur" :
				plateau[0][1] = "O"
		if colonne == 2 :
			if joueur == "IA" :
				plateau[0][2] = "X"
			if joueur == "joueur" :
				plateau[0][2] = "O"
	if ligne == 1 :
		if colonne == 0 :
			if joueur == "IA" :
				plateau[1][0] = "X"
			if joueur == "joueur" :
				plateau[1][0] = "O"
		if colonne == 1 :
			if joueur == "IA" :
				plateau[1][1] = "X"
			if joueur == "joueur" :
				plateau[1][1] = "O"
		if colonne == 2 :
			if joueur == "IA" :
				plateau[1][2] = "X"
			if joueur == "joueur" :
				plateau[1][2] = "O"
	if ligne == 2 :
		if colonne == 0 :
			if joueur == "IA" :
				plateau[2][0] = "X"
			if joueur == "joueur" :
				plateau[2][0] = "O"
		if colonne == 1 :
			if joueur == "IA" :
				plateau[2][1] = "X"
			if joueur == "joueur" :
				plateau[2][1] = "O"
		if colonne == 2 :
			if joueur == "IA" :
				plateau[2][2] = "X"
			if joueur == "joueur" :
				plateau[2][2] = "O"
	if joueur == "IA" :
		print("Les croix appartiennent à l'IA")
	afficher_plateau(plateau)
		
					
def verification_choix(ligne,colonne,plateau) :
		
	if plateau[ligne][colonne] == "X" :
		print("Case déjà choisie par l'IA")
	if plateau[ligne][colonne] == "O" :
		print("Case déjà choisie par vous")
			
			
def traduction(choix,plateau) :
		
	if choix == 1 :
		placer_valeur("joueur",0,0,plateau)
	if choix == 2 :
		placer_valeur("joueur",0,1,plateau)
	if choix == 3 :
		placer_valeur("joueur",0,2,plateau)
	if choix == 4 :
		placer_valeur("joueur",1,0,plateau)
	if choix == 5 :
		placer_valeur("joueur",1,1,plateau)
	if choix == 6 :
		placer_valeur("joueur",1,2,plateau)
	if choix == 7 :
		placer_valeur("joueur",2,0,plateau)
	if choix == 8 :
		placer_valeur("joueur",2,1,plateau)
	if choix == 9 :
		placer_valeur("joueur",2,2,plateau)		


def verification_demande() :
		
	choix = 0
	while not(1 <= choix <= 9) :
		choix = int(input("Choisissez un emplacement en écrivant le chiffre le représentant : "))
		return choix
		
def victoire() :
	print("L'IA a gagné")
	print("")
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	morpion()
			
def egalite() :
	print("Il y a égalité.")
	print("")
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	morpion()

def morpion() :
	
	plateau = [[1,2,3],[4,5,6],[7,8,9]]
	choix = 0
	print("IA morpion imbattable rapide")
	reponse = input("Appuyez sur o puis Entrée si vous voulez commencer, n puis Entrée si vous voulez que l'IA commence ou Entrée pour quitter : ")
	if reponse == "o" :
