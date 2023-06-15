import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from . import db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True)
  artist_id = db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
  startTime = db.Column(db.DateTime, default=datetime.utcnow)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    show_id = db.relationship('Show', backref='Venue')

    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    site = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    show_id = db.relationship('Show', backref='Artist')

    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image = db.Column(db.String(500))
    genres = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    site = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))