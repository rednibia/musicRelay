from configparser import ConfigParser
from sqlalchemy import create_engine


class MusicRepository(object):
    config = ConfigParser()
    config.read('config.ini')
    db_string = "postgres://{}:{}@{}:{}/music_lookup".format(
        config['postgresql']['user'], config['postgresql']['password'],
        config['postgresql']['url'], config['postgresql']['port'])
    db = create_engine(db_string)

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
