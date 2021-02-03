from db import db 

class PlayerModel(db.Model):
    __tablename__ = "players"

    _id = db.Column(db.Integer, primary_key=True)
    screenname = db.Column(db.String(128), nullable=False)
    steamid = db.Column(db.String(128), nullable=False)

    def __init__(self, titlscreennamee, steamid):
        self.screenname = screenname
        self.steamid = steamid

    def json(self):
        return {'screen_name': self.screenname, 'steam_id': self.steamid}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(screenname=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()