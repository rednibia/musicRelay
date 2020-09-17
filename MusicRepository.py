from configparser import ConfigParser
from sqlalchemy import create_engine


class MusicRepository(object):
    config = ConfigParser()
    config.read('config.ini')
    db_string = "postgres://{}:{}@{}:{}/music_lookup".format(
        config['postgresql']['user'], config['postgresql']['password'],
        config['postgresql']['url'], config['postgresql']['port'])
    db = create_engine(db_string)

    def get_playlist(self, rfid):
        sql_statement = "select playlist from rfid_playlist_lookup where rfid='{}'".format(rfid)
        row = self.db.execute(sql_statement).fetchone()
        return row['playlist']
