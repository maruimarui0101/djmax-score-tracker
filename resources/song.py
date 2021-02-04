from flask_restful import Resource, Api
from models.song import SongModel
from flask_restful import reqparse

class Song(Resource):
    parser = reqparse.RequestParser()

    # parser.add_argument('title', type=str, required=True, help='Title of the song')
    parser.add_argument('artist', type=str, required=True, help='Artist of the song')
    parser.add_argument('pack', type=str, required=True, help='Pack name')

    def get(self, name):
        song = SongModel.find_by_name(name)
        print(song)
        if song:
            return song.json()
        
        return {'message': 'Song was not found'}, 404

    def post(self, name):
        data = Song.parser.parse_args()
        song = SongModel(name, **data)

        try:
            song.save_to_db()
            return {'message': 'Song successfully added'}, 200
        except:
            return {'message': 'Error adding song to database'}, 404

class SongAllList(Resource):
    def get(self):
        return {'songs': list(map(lambda x: x.json(), SongModel.query.all()))}

class SongPackList(Resource):
    def get(self, pack):
        return {'songs': list(map(lambda x: x.json(), SongModel.query.filter_by(pack=pack)))}