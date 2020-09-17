from MusicRepository import MusicRepository


class PlaylistProcessor:

    music_repository = MusicRepository()
    playlists = music_repository.get_playlists()

    def reset_playlists(self):
        self.playlists = MusicRepository.get_playlists()

    def get_playlist(self, rfid):
        if rfid not in self.playlists.keys():
            self.playlists[rfid] = MusicRepository.get_playlist(rfid)
        return self.playlists[rfid]
