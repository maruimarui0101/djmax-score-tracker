import os
from instance.config import app_config
from flask import Flask
from flask_restful import Resource, Api
from resources.song import Song, SongAllList, SongPackList


def create_app(config_name):
    """Creates instance of the application with defined config from env variables."""
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # adding resources 
    api.add_resource(Song, '/song/<string:name>')
    api.add_resource(SongAllList, '/allsongs')
    # api.add_resource(SongPackList, '/song/pack/<string:pack>')


    from db import db 
    db.init_app(app)

    return app
