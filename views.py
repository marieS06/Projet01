##% controleur ##
from crypt import methods
from select import select
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from app import db
from app import app
from models import Credit, Institution, Passion
from flask import redirect
from models import Centre

@app.route('/')
def home():
    return render_template("accueil.html")

@app.route('/formulaire')
def formulaire():

   return render_template("formulaire.html")

@app.route('/monProfil', methods=['POST'])
def monProfil():

   if request.method == "POST":

      education = request.form['education']
      
      nomPassion = request.form['nomPassion']

      credit_card_type = request.form['credit_card_type']
      
      result = Centre.query.join(Institution).join(Passion).join(Credit).filter(Institution.idInstitution==education).filter(
      Passion.idPassion== nomPassion).filter(Credit.idBank==credit_card_type).all()
      
      print(result)
   return render_template("monProfil.html", education=education,nomPassion=nomPassion, credit_card_type=credit_card_type,result=result)

# select candidate from centre inner join centre.idInstitution = institution.idInstitution innerjoin
# passion.idPassion = centre.idPassion inner join credit.idBank=centre.idBank where centre.idInstitution = education
# and centre.idPassion = nomPassion and centre.idBank = credit_card_type

