# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : generateur de phrases
# Utilisation :  generateur.py

import os
import sys
import random

class main:

	determinants = list(open(r'dictionnaires\determinants.txt', "rb").read().splitlines())
	negatif = list(open(r'dictionnaires\negatif.txt', "rb").read().splitlines())
	positif = list(open(r'dictionnaires\positif.txt', "rb").read().splitlines())
	sujet_verbe = list(open(r'dictionnaires\sujet_verbe.txt', "rb").read().splitlines())
	noms_communs = list(open(r'dictionnaires\noms_communs.txt', "rb").read().splitlines())
	liste_resultat=[]
	
	i=1
	while i<= 10:
		phrase=random.choice(sujet_verbe)+' '+random.choice(determinants)+' '+random.choice(positif)+' '+random.choice(noms_communs).split(',')[0]
		liste_resultat.append(phrase)
		print phrase
		i=i+1

	resultat = open('resultat.txt', "w")
	resultat.write('\n'.join(liste_resultat))
	print '\nResultat : '+ resultat.name
