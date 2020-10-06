from MusicRepository import MusicRepository


class ClientProcessor:

    music_repository = MusicRepository()
    locations = music_repository.get_locations()

    def reset_locations(self):
        self.locations = MusicRepository.get_locations()

    def get_location(self, client_id):
        if client_id not in self.locations.keys():
            self.locations[client_id] = MusicRepository.get_location(client_id)
        return self.locations[client_id]
