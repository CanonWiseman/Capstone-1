# Imports here
from flask import Flask, request, render_template, redirect, flash, session, jsonify, current_app, _app_ctx_stack
from models import db, connect_db, Test
from flask_debugtoolbar import DebugToolbarExtension

#creates flask app wuth the secret key for debugging
app = Flask(__name__)

app.config['SECRET_KEY'] = "1234"

# #only for flask debug toolbar 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# #only for flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Spartacus97@localHost:5432/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
with app.app_context():
    db.create_all()

#routes here

@app.route("/")
def index():
    return render_template("index.html")

