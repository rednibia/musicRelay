from ClientProcessor import ClientProcessor
from MusicPlayer import MusicPlayer
from PlaylistProcessor import PlaylistProcessor


class MusicProcessor(object):

    client_processor = ClientProcessor()
    playlist_processor = PlaylistProcessor()
    music_player = MusicPlayer()

    def play(self, rfid, client_id, play_mode=None):
        try:
            location = self.client_processor.get_location(client_id)
            print("Playing music in location: " + str(location))
            playlist = self.playlist_processor.get_playlist(rfid)
            print("Playing playlist: " + playlist)
            self.music_player.play(playlist, location, play_mode)
        except TypeError:
            print("Issue With Client ID: {}, RF ID: {}".format(client_id, rfid))
            new_playlist = input("Playlist Name:")
            if len(new_playlist) > 0:
                result = self.playlist_processor.add_playlist(new_playlist, rfid)
                print(result)

    def command(self, command, client_id):
        location = self.client_processor.get_location(client_id)
        print("Running command in location: " + str(location))
        if command == "volume_up":
            self.music_player.volume_up(location)
        if command == "volume_down":
            self.music_player.volume_down(location)
