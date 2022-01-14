from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
## app tu te trouves dans ce chemin
