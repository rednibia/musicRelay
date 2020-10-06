from ClientProcessor import ClientProcessor
from MusicPlayer import MusicPlayer
from PlaylistProcessor import PlaylistProcessor


class MusicProcessor(object):

    client_processor = ClientProcessor()
    playlist_processor = PlaylistProcessor()
    music_player = MusicPlayer()

    def play(self, rfid, client_id, play_mode=None):
        locations = self.client_processor.get_locations(client_id)
        playlist = self.playlist_processor.get_playlist(rfid)
        self.music_player.play(playlist, locations, play_mode)
