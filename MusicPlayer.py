from MusicRepository import MusicRepository
from soco import SoCo


class MusicPlayer:

    music_repository = MusicRepository()
    ips = music_repository.get_ips()
    sonos = SoCo(ips["Gym"])
    playlists = dict()
    for favorite in sonos.music_library.get_sonos_favorites():
        playlists[favorite.title] = favorite.reference

    # VALID PLAY MODES
    # ('NORMAL', 'SHUFFLE_NOREPEAT', 'SHUFFLE', 'REPEAT_ALL',
    #           'SHUFFLE_REPEAT_ONE', 'REPEAT_ONE')
    def play(self, playlist, location, play_mode):
        print("PLAY MODE: " + str(play_mode))
        if playlist not in self.playlists.keys():
            self.playlists = dict()
            for favorite in self.sonos.music_library.get_sonos_favorites():
                self.playlists[favorite.title] = favorite.reference
        try:
            for speaker in location:
                if speaker not in self.ips:
                    self.ips = self.music_repository.get_ip(speaker)
                print("Playing on Speaker with IP Address: " + self.ips[speaker])
                sonos = SoCo(self.ips[speaker])
                sonos.clear_queue()
                sonos.add_to_queue(self.playlists[playlist])
                if play_mode is not None:
                    sonos.play_mode = play_mode
                else:
                    sonos.play_mode = 'NORMAL'
                sonos.play_from_queue(0)
        except KeyError:
            print("Trouble with Playlist: {}, Location {}, Play_Mode: {}".format(playlist,
                                                                                 location, play_mode))
