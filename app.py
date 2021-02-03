from flask import Flask
from flask_restful import Resource, Api
from resources.song import Song, SongAllList, SongPackList
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


#config 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Song, '/song/<string:name>')
api.add_resource(SongAllList, '/song/all')
api.add_resource(SongPackList, '/song/pack/<string:pack>,')


if __name__ == '__main__':
    from db import db 
    db.init_app(app)
    app.run(debug=True)