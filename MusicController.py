from flask_restful import Resource, reqparse
from MusicPlayer import MusicPlayer


class MusicController(Resource):

    parser = reqparse.RequestParser()
    music_player = MusicPlayer()

    def post(self):
        self.parser.add_argument("rfid")
        self.parser.add_argument("location")
        args = self.parser.parse_args()
        self.music_player.play(args["rfid"], args["location"])
