import os


class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marie:marie@localhost:5432/cle'
    print("Successfully connected!")
    

   