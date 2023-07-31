import os, secrets

class Config(object):
    SECRET_KEY = os.urandom(32)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://gabrielacosta@localhost/fyyur'

    
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

