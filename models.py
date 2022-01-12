from app import db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Candidate(db.Model):
   __tablename__='candidate'
    
   idU = db.Column(db.Integer, primary_key=True)
   Candidates = db.Column(db.String(64))
   Gender = db.Column(db.Boolean, default=False, nullable=False)

   def __init__(self, Candidates):
      
      self.Candidates = Candidates
   
   def __repr__(self):
      return f"{self.Candidate}"

class Credit_card_type(db.Model):
   __tablename__='credit_card_type'

   idh = db.Column(db.Integer, primary_key=True)
   idBank = db.Column(db.Integer, primary_key=True)
   credit_card_types = db.Column(db.String(64))

   def __init__(self, credit_card_types):
      
      self.credit_card_types = credit_card_types
   
   def __repr__(self):
      return f"{self.credit_card_types}"

class Passion(db.Model):
   __tablename__='passion'
    
   id = db.Column(db.Integer, primary_key=True)
   passions = db.Column(db.String(64))

   def __init__(self, passions):
      
      self.banque = passions
   
   def __repr__(self):
      return f"{self.passions}"

class Educational_institution(db.Model):
   __tablename__='educational_institution'
    
   id = db.Column(db.Integer, primary_key=True)
   educ = db.Column(db.String(64))

   def __init__(self, educ):
      
      self.banque = educ
   
   def __repr__(self):
      return f"{self.educ}"




