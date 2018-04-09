from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form', methods=['POST'])
def form():
	print(request.form.get('nom', 'valeur par défaut'))
    return 'Validé' 

@app.route('/base')
def hello():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
