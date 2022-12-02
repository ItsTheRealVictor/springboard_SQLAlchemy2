from flask import Flask, request, render_template, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
# from models import Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# class Pet(db.Model):
#     __tablename__ = 'pets'
    
#     id = db.Column(db.Integer,
#                    primary_key=True,
#                    autoincrement=True)
    
#     name = db.Column(db.String(50), 
#                      nullable=False,
#                      unique=True)
    
#     species = db.Column(db.String(30), nullable=True)
    
#     hunger = db.Column(db.Integer, nullable=False, default=True)



# db.create_all()
# and_another_example_pet = Pet(id=7, name='kldjfa;lsdkfja;sldk', species='sadfglksjdfgl;ksjdf', hunger=34)
# db.session.add(and_another_example_pet)
# db.session.commit()

@app.route('/')
def main_page():
  return render_template('home.html')
