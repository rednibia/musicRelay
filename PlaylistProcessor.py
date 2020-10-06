from MusicRepository import MusicRepository


class PlaylistProcessor:

    music_repository = MusicRepository()
    playlists = music_repository.get_playlists()

    def reset_playlists(self):
        self.playlists = self.music_repository.get_playlists()

    def get_playlist(self, rfid):
        if rfid not in self.playlists.keys():
            self.playlists[rfid] = self.music_repository.get_playlist(rfid)
        return self.playlists[rfid]
