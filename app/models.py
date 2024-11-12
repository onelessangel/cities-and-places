from . import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    is_favourite = db.Column(db.Boolean, nullable=False)
    is_visited = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.String(100), nullable=True)
