from flask_restful import Resource, reqparse
from MusicProcessor import MusicProcessor


class MusicController(Resource):

    parser = reqparse.RequestParser()
    music_processor = MusicProcessor()

    def post(self):
        self.parser.add_argument("rfid")
        self.parser.add_argument("location")
        args = self.parser.parse_args()
        self.music_processor.play(args["rfid"], args["location"])
