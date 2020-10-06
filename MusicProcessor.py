from MusicPlayer import MusicPlayer
from PlaylistProcessor import PlaylistProcessor


class MusicProcessor(object):

    playlist_processor = PlaylistProcessor()
    music_player = MusicPlayer()

    def play(self, rfid, location, play_mode=None):
        playlist = self.playlist_processor.get_playlist(rfid)
        self.music_player.play(playlist, location, play_mode)
