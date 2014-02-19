__author__ = 'aahammer'

from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID

engine = create_engine('postgresql://postgres:1234@localhost:5432/smite')
metadata = MetaData(engine, schema="stats")


match = Table('match', metadata,
    Column('match_id', Integer, primary_key = True),
    Column('queue_type', VARCHAR(32)),
    Column('match_type',  VARCHAR(32)),
    Column('duration', Integer),
    Column('end_time',  TIMESTAMP)
)

player = Table('player', metadata,
    Column('name', VARCHAR(64), primary_key = True),
    Column('match_id', Integer, ForeignKey('match.match_id'), primary_key = True),
    Column('level', SMALLINT),
    Column('god', VARCHAR(64)),
    Column('kills',  SMALLINT),
    Column('deaths', SMALLINT),
    Column('assists', SMALLINT),
    Column('gold', Integer ),
    Column('damage_player', Integer ),
    Column('damage_structure', Integer ),
    Column('damage_creep', Integer ),
    Column('damage_taken', Integer ),
    Column('healing', Integer ),
    Column('item1', Integer ),
    Column('item2', Integer ),
    Column('item3', Integer ),
    Column('item4', Integer ),
    Column('item5', Integer ),
    Column('item6', Integer ),
    Column('active1', Integer ),
    Column('active2', Integer )
)

metadata.create_all()