from db import db 

class SongModel(db.Model):
    __tablename__ = "songs"

    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    pack = db.Column(db.String(128), nullable=False)

    def __init__(self, title, artist, pack):
        self.title = title
        self.artist = artist
        self.pack = pack

    def json(self):
        return {'title': self.title, 'artist': self.artist, 'pack': self.pack}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(title=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        