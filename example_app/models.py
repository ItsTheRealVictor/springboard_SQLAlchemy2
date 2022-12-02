from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
db.create_all()
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
    
    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()    
    
    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()
    
    def __repr__(self):
        return f'Pet: {self.id } {self.name} of species {self.species}'
    
    def feed(self, amount=20):
        self.hunger -= amount
        self.hunger = max(self.hunger, 0)
    

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


# querying

# Pet.query.get(7)
# gets the pet with id of 7 (get() method works with primary key)


# pass in keyword arguments with filter_by() (use filter_by() to filter based on equality)
# Pet.query.filter_by(name='third').all()

# use filter() for more complex queries
# Pet.query.filter(Pet.hunger > 5).all()
    # instead of .all() 
        # .get(pk) > get single record with that primary key value
        # .all() > get all records as a list
        # .first()  > get first record or None
        # .one() > get first record, error if 0 or if greater than 1.


# customizing models

