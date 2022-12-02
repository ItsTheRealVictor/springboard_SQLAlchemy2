from flask_debugtoolbar import DebugToolbarExtension
from models import app, db, Pet
from flask import request, render_template, redirect, url_for, flash


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = "farts"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
# db.create_all()

pets = Pet.query.all()
print(pets)
# @app.route('/')
# def list_pets():
#     pets = Pet.query.all()
#     return render_template('index.html', pets=pets)


