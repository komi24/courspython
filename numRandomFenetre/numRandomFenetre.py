#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 


class MaFenetre:
	def grand_bouton_handler(self):
		self.ecranMessage.itemconfigure(self.textMessage, text="okok")
		print("hello")

	def __init__(self):
		fenetre = Tk() 
		
		self.label = Label(fenetre, text="Chiffre à trouver") 
		self.label.pack() 

		self.ecranMessage = Canvas(fenetre, width=250, height=50, bg='ivory')
		self.textMessage = self.ecranMessage.create_text(100,25, text="testfb", justify=CENTER)
		self.ecranMessage.pack(side=LEFT, padx=5, pady=5)
		
		self.grand_bouton = Button(fenetre, text ='Trop grand', command= self.grand_bouton_handler)
		self.grand_bouton.pack(side=TOP, padx=5, pady=5) 
		
		self.petit_bouton = Button(fenetre, text ='trop petit')
		self.petit_bouton.pack(padx=5, pady=5)
		
		self.bouton_bon_resultat = Button(fenetre, text ='Bon résultat')
		self.bouton_bon_resultat.pack(side=BOTTOM, padx=5, pady=5)

		self.bouton_raz = Button(fenetre, text ='RAZ')
		self.bouton_raz.pack(side=BOTTOM, padx=5, pady=5)


		fenetre.mainloop()


if __name__  == "__main__":
	maFenetre = MaFenetre()
