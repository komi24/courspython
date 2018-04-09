#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Dico :

	def Dichop(self,proposition,bornebasse, bornehaute):
				self.bornebasse=proposition
				self.proposition=random.randint(bornebasse,bornehaute)
				label=Label(fenetre, text="Voici la valeur proposee : "+str(proposition))
				label.pack()
				
			   
					
					
	def Dichog(self,proposition,bornebasse, bornehaute):
				self.bornehaute=proposition
				self.proposition=random.randint(bornebasse,bornehaute)
				label=Label(fenetre, text="Voici la valeur proposee : "+str(proposition))
				label.pack()
			   

			reponse=input("Est ce la bonne reponse (p pour trop petit ou g pour trop grand ou o pour bonne reponse)")
			
	def Dichoo(self,proposition):			
		
		label=Label(fenetre, text="BRAVO : "+str(proposition))
				label.pack()
