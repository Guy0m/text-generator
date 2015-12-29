# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : Supprimer les doublons et classer les mots d'un dictionnaire
# Utilisation :  trier.py fichier.txt

import os
import sys

class main:

	fichier = open(sys.argv[1], "rb")
	lignes = list(fichier.read().splitlines())
	nb_lignes = len(lignes)
	print '\nLe fichier',fichier.name,'contient' ,len(lignes),' mots.'
	
	#Suppression des doublons
	lignes=list(set(lignes))
	print '\n',nb_lignes-len(lignes),' doublons detectes et supprimes'
	
	#Tri par ordre alphabetique
	lignes.sort()
	print '\n',len(lignes),'mots tries par ordre alphabetique'

	resultat = open(sys.argv[1]+'.tri.txt', "w")
	resultat.write('\n'.join(lignes))
	print '\nResultat : '+ resultat.name
