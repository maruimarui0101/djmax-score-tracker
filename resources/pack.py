from flask_restful import Resource, Api
from models.pack import PackModel
from flask_restful import reqparse

class Pack(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name', type=str, required=True, help='Title of the song')
    parser.add_argument('released', type=str, required=True, help='Artist of the song')
    parser.add_argument('collab', type=bool, required=True, help='Pack name')

    def get(self, name):
        pack = PackModel.find_by_name(name)
        print(pack)
        if pack:
            return pack.json()
        
        return {'message': 'Song was not found'}, 404

    def post(self, name):
        data = Pack.parser.parse_args()
        pack = PackModel(**data)

        try:
            pack.save_to_db()
        except:
            return {'message': 'Error adding song to database'}, 404

class PackAllList(Resource):
    def get(self):
        return {'packs': list(map(lambda x: x.json(), PackModel.query.all()))}
