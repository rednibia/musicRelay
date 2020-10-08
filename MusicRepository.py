from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import sessionmaker


class Playlist(Base):
    __tablename__ = "rfid_playlist_lookup"

    rfid = Column(String, primary_key=True)
    playlist = Column(String, primary_key=True)


class MusicRepository(object):
    config = ConfigParser()
    config.read('config.ini')
    db_string = "postgres://{}:{}@{}:{}/music_lookup".format(
        config['postgresql']['user'], config['postgresql']['password'],
        config['postgresql']['url'], config['postgresql']['port'])
    db = create_engine(db_string)
    Session = sessionmaker(bind=db)
    session = Session()

    def get_playlists(self):
        playlists = dict()
        sql_statement = "select rfid, playlist from rfid_playlist_lookup"
        rows = self.db.execute(sql_statement)
        for row in rows:
            playlists[row['rfid']] = row['playlist']
        return playlists

    def get_playlist(self, rfid):
        sql_statement = "select playlist from rfid_playlist_lookup where rfid='{}'".format(rfid)
        row = self.db.execute(sql_statement).fetchone()
        return row['playlist']

    def add_playlist(self, new_playlist, rfid):
        playlist_row = Playlist(rfid=rfid, playlist=new_playlist)
        self.session.add(playlist_row)
        self.session.commit()

    def get_ips(self):
        ips = dict()
        sql_statement = "select sonos, ip_address from sonos_ip_lookup"
        rows = self.db.execute(sql_statement)
        for row in rows:
            ips[row['sonos']] = row['ip_address']
        return ips

    def get_ip(self, sonos):
        sql_statement = "select ip_address from sonos_ip_lookup where sonos='{}'".format(sonos)
        row = self.db.execute(sql_statement).fetchone()
        return row['ip_address']

    def get_locations(self):
        locations = dict()
        sql_statement = "select location, client_id from client_location_lookup"
        rows = self.db.execute(sql_statement)
        for row in rows:
            if row['client_id'] not in locations.keys():
                locations[row['client_id']] = set()
            locations[row['client_id']].add(row['location'])
        return locations

    def get_location(self, client_id):
        sql_statement = "select location from client_location_lookup where client_id='{}'".format(client_id)
        rows = self.db.execute(sql_statement)
        locations = set()
        for row in rows:
            locations.add(row['location'])
        return locations
