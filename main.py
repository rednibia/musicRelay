from flask import Flask
from flask_restful import Api
from MusicPlayer import MusicPlayer


app = Flask(__name__)
api = Api(app)
api.add_resource(MusicPlayer, '/play/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
