from db import db
from sqlalchemy import Table, Column, Integer, ForeignKey,String,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


import pandas as pd

class Credit(db.Model):
   __tablename__='credit'

   idBank = db.Column(db.Integer, primary_key=True)
   credit_card_type = db.Column(db.String(64))
   credit = relationship("Centre")
   
   
   def center(engine):
      enter = pd.read_csv('credit.csv')
      enter.to_sql('credit',engine, if_exists='append',index=False, chunksize=1 )


class Passion(db.Model):
   __tablename__='passion'
    
   idPassion = db.Column(db.Integer, primary_key=True)
   nomPassion = db.Column(db.String(64))
   passion = relationship("Centre")

   
   def center(engine):
      enter = pd.read_csv('passion.csv')
      enter.to_sql('passion',engine, if_exists='append',index=False, chunksize=1 )


class Institution(db.Model):
   __tablename__='institution'
    
   idInstitution = db.Column(db.Integer, primary_key=True)
   Education = db.Column(db.String(64))
   institution = relationship("Centre")      


   def center(engine):
      enter = pd.read_csv('institution.csv')
      enter.to_sql('institution',engine, if_exists='append',index=False, chunksize=1)

class Centre(db.Model):
   __tablename__='centre'
    
   ID = db.Column(db.Integer, primary_key=True)
   Candidate = db.Column(db.String(64))
   Gender = db.Column(db.String(64))
   idBank = db.Column(db.Integer,ForeignKey('credit.idBank'))
   idPassion = db.Column(db.Integer,ForeignKey('passion.idPassion'))
   idInstitution = db.Column(db.Integer,ForeignKey('institution.idInstitution'))


   def center(engine):
      enter = pd.read_csv('Centre.csv')
      enter.to_sql('centre',engine,if_exists='append',index=False, chunksize=1)




