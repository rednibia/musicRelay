from flask_restful import Resource, reqparse


class MusicPlayer(Resource):

    parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument("playlist")
        self.parser.add_argument("location")
        args = self.parser.parse_args()
        print("playlist: " + args["playlist"])
        print("location: " + args["location"])
