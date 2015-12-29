# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : generateur de phrases
# Utilisation :  generateur.py

import os
import sys
import random

class main:

	liste_determinants = list(open(r'dictionnaires\determinants.txt', "rb").read().splitlines())
	liste_negatif = list(open(r'dictionnaires\negatif.txt', "rb").read().splitlines())
	liste_positif = list(open(r'dictionnaires\positif.txt', "rb").read().splitlines())
	liste_sujet_verbe = list(open(r'dictionnaires\sujet_verbe.txt', "rb").read().splitlines())
	liste_noms_communs = list(open(r'dictionnaires\noms_communs.txt', "rb").read().splitlines())
	liste_resultat=[]
	choix = 'null'
	determinant = 'null,null'
	nom_commun = 'null,null'
	positif = 'null,null'
	negatif = 'null,null'
	classification = ['masculin', 'feminin'] #'neutre', 'pluriel', 'voyelle'
	tendance = 50; #tendance negative a 100, neutre a 50, positive a 0
	
	i=1
	while i<= 15:
		
		
		if choix == 'null':
			choix = random.choice(classification)

		while choix !=  determinant.split(',')[1]:
			determinant=random.choice(liste_determinants)
		
		if tendance < random.randint(0,100):		
			while choix !=  positif.split(',')[1]:
				positif=random.choice(liste_positif)
				adjectif=positif
			
		else:
			while choix !=  negatif.split(',')[1]:
				negatif=random.choice(liste_negatif)
				adjectif=negatif
		
		while choix !=  nom_commun.split(',')[1]:
			nom_commun=random.choice(liste_noms_communs)
			
		phrase=random.choice(liste_sujet_verbe)+' '+determinant.split(',')[0]+' '+adjectif.split(',')[0]+' '+nom_commun.split(',')[0]
		liste_resultat.append(phrase)
		print phrase
		i=i+1
		choix = 'null'
		determinant = 'null,null'
		nom_commun = 'null,null'
		positif = 'null,null'
		
	resultat = open('resultat.txt', "w")
	resultat.write('\n'.join(liste_resultat))
	print '\nResultat : '+ resultat.name
