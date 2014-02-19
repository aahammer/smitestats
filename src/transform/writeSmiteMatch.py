__author__ = 'aahammer'

from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID


ENGINE = create_engine('postgresql://postgres:1234@localhost:5432/smite')
METADATA = MetaData(ENGINE, schema="stats")

def writeMatchData(data):

    match_table = Table('match', METADATA, autoload=True)
    res = insert(match_table).values(data)
    res.execute()


def writePlayerData(data):

    player_table = Table('player', METADATA, autoload=True)
    res = insert(player_table).values(data)
    res.execute()