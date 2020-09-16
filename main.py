from flask import Flask
from flask_restful import Resource, Api, reqparse
from MusicPlayer import MusicPlayer


app = Flask(__name__)
api = Api(app)
api.add_resource(MusicPlayer, '/play/')

if __name__ == "__main__":
  app.run(debug=True)
