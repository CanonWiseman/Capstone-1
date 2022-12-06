from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

#models go here

class Test(db.Model):
    """Pet."""

    __tablename__ = 'table_name here'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    col_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    

    #additional methods go here