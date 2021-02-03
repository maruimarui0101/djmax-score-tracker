# NOTE: found out that VSC does not support type hinting (Python 3.7+ feature)

from db import db 

class ScoreModel(db.Model):
    __tablename__ = "scores"

    _id = db.Column(db.Integer, primary_key=True)
    chartid = db.Column(db.String(128), nullable=False) # needs relationship
    max100 = db.Column(db.Integer, nullable=False) 
    max90 = db.Column(db.Integer, nullable=False) 
    max80 = db.Column(db.Integer, nullable=False) 
    max70 = db.Column(db.Integer, nullable=False) 
    max60 = db.Column(db.Integer, nullable=False) 
    max50 = db.Column(db.Integer, nullable=False) 
    max40 = db.Column(db.Integer, nullable=False) 
    max30 = db.Column(db.Integer, nullable=False) 
    max20 = db.Column(db.Integer, nullable=False) 
    max10 = db.Column(db.Integer, nullable=False) 
    max1 = db.Column(db.Integer, nullable=False) 
    _break = db.Column(db.Integer, nullable=False) # break is python reserve word


    def __init__(self, chartid, max100: int, max90: int, max80: int, max70: int, max60: int, max50: int, max40: int, max30: int, max20: int, max10: int, max1: int, _break: int):
        self.chartid = chartid
        self.max100 = max100
        self.max90 = max90
        self.max80 = max80
        self.max70 = max70
        self.max60 = max60
        self.max50 = max50
        self.max40 = max40
        self.max30 = max30
        self.max20 = max20
        self.max10 = max10
        self.max1 = max1
        self._break = _break

    # each note has a base score
    NOTE_BASE_SCORE = 300000

    # function to calculate the raw score 
    def calc_perc(max100: int, max90: int, max80: int, max70: int, max60: int, max50: int, max40: int, max30: int, max20: int, max10: int, max1):
        """
        Calculation of percentage 
        """

        return 0

    # make a function that will calculate raw score
    def calc_score(max100: int, max90: int, max80: int, max70: int, max60: int, max50: int, max40: int, max30: int, max20: int, max10: int, max1):  
        """
        Calculates score based on accuracy of individual notes
        reference material https://www.reddit.com/r/djmax/comments/6rpznw/scoring_on_djmax_respect/
        """

        multiplier = 1
        NOTE_BASE_SCORE*multiplier

        return 0.0

    # make function that verifies that note count is equal 
    def note_count_verify(max100: int, max90: int, max80: int, max70: int, max60: int, max50: int, max40: int, max30: int, max20: int, max10: int, max1: int, _break: int):
        """"
        Verification of note count entered in post request
        """
        return None

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

# classes to make, Scores by day, Best Scores, Score by Player
