from app import db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Centre(db.Model):
   __tablename__='centre'
    
   ID = db.Column(db.Integer, primary_key=True)
   Candidates = db.Column(db.String(64))
   Gender = db.Column(db.Boolean, default=False, nullable=False)
   idBank = db.Column(db.Integer)
   idPassion = db.Column(db.Integer)
   idInstitution = db.Column(db.Integer)

   def __init__(self, Candidates):
      
      self.Candidates = Candidates
   
   def __repr__(self):
      return f"{self.Candidates}"

class Credit (db.Model):
   __tablename__='credit'

   idBank = db.Column(db.Integer, primary_key=True)
   credit_card_type = db.Column(db.String(64))

   def __init__(self, credit_card_type):
      
      self.credit_card_type = credit_card_type
   
   def __repr__(self):
      return f"{self.credit_card_type}"

class Passion(db.Model):
   __tablename__='passion'
    
   idPassion = db.Column(db.Integer, primary_key=True)
   nomPassion = db.Column(db.String(64))

   def __init__(self, nomPassion):
      
      self.nomPassion = nomPassion
   
   def __repr__(self):
      return f"{self.nomPassion}"

class Institution(db.Model):
   __tablename__='institution'
    
   idInstitution = db.Column(db.Integer, primary_key=True)
   Education = db.Column(db.String(64))

   def __init__(self, Education):
      
      self.Education = Education
   
   def __repr__(self):
      return f"{self.Education}"




