from Database import Database


class MusicPlayer(object):

    database = Database()

    def play(self, rfid, location):
        playlist = self.database.get_playlist(rfid)
        print(playlist)
