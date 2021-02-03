from db import db 
from datetime import datetime

class PackModel(db.Model):
    __tablename__ = "packs"

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    released = db.Column(db.DateTime, nullable=False)
    collab = db.Column(db.Boolean, nullable=False) # some packs are recognised under collab category in game

    def __init__(self, name, released. collab):
        self.name = name
        self.released = released # need to see how to parse datetime in json
        self.collab = collab

    def json(self):
        return {'name': self.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

