from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

class Narrative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
