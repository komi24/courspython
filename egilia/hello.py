from flask import Flask
from flask import render_template
from flask import request
from MonPackage import db
from MonPackage.Personne import Personne

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personnes.sqlite3'

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/import-csv')
def import_csv():
	Personne.import_csv()
	return render_template('index.html')

@app.route('/users')
def list_users():
	print(Personne.query.all())
	users= Personne.query.filter_by(nom='Bolnet').all()
	return render_template('users.html', liste=users)

@app.route('/monform', methods=["POST"])
def monform():
	print(request.form['nom'])
	une_personne = Personne(request.form['nom'], request.form['prenom'])
	db.session.add(une_personne)
	db.session.commit()
	return "Formulaire validé"

