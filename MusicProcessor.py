from MusicRepository import MusicRepository
from MessageSender import Message_Sender


class MusicProcessor(object):

    music_repository = MusicRepository()
    message_sender = Message_Sender()

    def play(self, rfid, location):
        playlist = self.music_repository.get_playlist(rfid)
        self.message_sender.send(playlist, location)
