##% controleur ##
from flask import Flask
from flask import render_template, request, url_for
from app import db
from app import app

from flask import redirect

@app.route('/')
def home():
    return render_template("accueil.html")

@app.route('/formulaire')
def formulaire():
    return render_template("formulaire.html")


