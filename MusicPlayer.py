from flask_restful import Resource


class MusicPlayer(Resource):

    def post(self, playlist, location):
        print("playlist: " + playlist)
        print("location: " + location)
        pass
