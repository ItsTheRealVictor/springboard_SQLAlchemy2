from flask_sqlalchemy import SQLAlchemy
from app import db


# models go here

class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(50), 
                     nullable=False,
                     unique=True)
    
    species = db.Column(db.String(30), nullable=True)
    
    hunger = db.Column(db.Integer, nullable=False, default=True)
    

names = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth'
]
species = [
    'llkjsdflkjsdf',
    'bbbasdflkjksdfl',
    'ooweitruwoeiruweor',
    'hdhdsfkljshdkfjhs',
    'ljsldkfjsdflkj'
]

together = [Pet(name=n, species=s) for n, s in zip(names, species)]
# to insert all of these, in the terminal
# >>> from app import db, app
# >>> from models import Pet, together
# >>> db.session.add_all(together)
# >>> db.session.commit()