#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
fenetre = Tk()
import random
from Package.dicothomie_class import *
bornebasse=0
bornehaute=101
proposition=random.randint(bornebasse,bornehaute)

label=Label(fenetre, text="Voici la valeur proposee : "+str(proposition))
label.pack()
Button(fenetre, text ='Trop petit',command=dicothomie_class.Dichop).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Trop grand',command=dicothomie_class.Dichog).pack(side=BOTTOM, padx=5, pady=5)
Button(fenetre, text ='Bonne reponse!',command=dicothomie_class.Dichoo).pack(side=TOP, padx=10, pady=10)
bouton_quitter=Button(fenetre, text ='Arreter',command=fenetre.quit).pack(side=BOTTOM, padx=10, pady=10)

fenetre.mainloop()






