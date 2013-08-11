from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
freestyle_int = Table('freestyle_int', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('speed', String(length=64)),
    Column('a25', String(length=64)),
    Column('a50', String(length=64)),
    Column('a75', String(length=64)),
    Column('a100', String(length=64)),
    Column('a125', String(length=64)),
    Column('a150', String(length=64)),
    Column('a175', String(length=64)),
    Column('a200', String(length=64)),
    Column('a225', String(length=64)),
    Column('a250', String(length=64)),
    Column('a275', String(length=64)),
    Column('a300', String(length=64)),
    Column('a400', String(length=64)),
    Column('a500', String(length=64)),
    Column('a600', String(length=64)),
    Column('a700', String(length=64)),
    Column('a800', String(length=64)),
    Column('a900', String(length=64)),
    Column('a1000', String(length=64)),
    Column('a1650', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['freestyle_int'].columns['speed'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['freestyle_int'].columns['speed'].drop()
