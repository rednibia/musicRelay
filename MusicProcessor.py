from ClientProcessor import ClientProcessor
from MusicPlayer import MusicPlayer
from PlaylistProcessor import PlaylistProcessor


class MusicProcessor(object):

    client_processor = ClientProcessor()
    playlist_processor = PlaylistProcessor()
    music_player = MusicPlayer()

    def play(self, rfid, client_id, play_mode=None):
        location = self.client_processor.get_location(client_id)
        print("Playing music in location: " + location)
        playlist = self.playlist_processor.get_playlist(rfid)
        print("Playing playlist: " + playlist)
        self.music_player.play(playlist, location, play_mode)
