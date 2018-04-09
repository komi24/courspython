import csv
from flask_sqlalchemy import SQLAlchemy
from . import db


class Personne(db.Model):
	id = db.Column('person_id', db.Integer, primary_key= True)
	nom = db.Column(db.String(100))
	prenom = db.Column(db.String(100))
	def __init__(self, nom, prenom):
		self.nom= nom
		self.prenom= prenom
	
	def __str__(self):
		return "Personne : %s %s"%(self.prenom, self.nom)

	def __repr__(self):
		return "Personne : %s %s"%(self.prenom, self.nom)

	def save_egilia(self):
		with open("save.txt", "a") as file:
			writer = csv.writer(file)
			writer.writerow([self.nom, self.prenom])

	@staticmethod
	def import_csv():
		with open("save.txt", "r") as file:
			reader = csv.reader(file)
			users = [db.session.add(Personne(user[0],user[1])) for user in reader if len(user)>=2]
			db.session.commit()

	@staticmethod
	def list_users():
		with open("save.txt", "r") as file:
			reader = csv.reader(file)
			return [Personne(user[0],user[1]) for user in reader if len(user)>=2]

