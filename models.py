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
    

# example_pet = Pet(id=2, name='example', species='farter', hunger=10)
# db.session.add(example_pet)
# db.session.commit()