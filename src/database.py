import psycopg2
from flask import current_app, g
from flask.cli import with_appcontext

from . import db

from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, MONEY, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

from sqlalchemy.schema import Column, ForeignKey

class FederatedInstances(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    registration_time = Column(TIMESTAMP)
    domain = Column(VARCHAR(512), unique=True)
    public_key = Column(VARCHAR(10000))

class Communities(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    name = Column(VARCHAR(48))
    distinguisher = Column(SMALLINT)

class Users(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    salt = Column(BIT(256))
    distinguisher = Column(SMALLINT)
    username = Column(VARCHAR(48))
    password = Column(VARCHAR(184))
    public_key = Column(VARCHAR(10000))
    private_key = Column(VARCHAR(10000))
    domain = Column(VARCHAR(512), ForeignKey('federated_instances.domain'))

class Posts(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    error_code = Column(SMALLINT)
    text = Column(VARCHAR(100000))
    url = Column(VARCHAR(32768))
    author = Column(BIGINT, ForeignKey('users.id'))
    community = Column(BIGINT, ForeignKey('communities.id'))

class PostVotes(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    post = Column(BIGINT, ForeignKey('posts.id'))
    user = Column(BIGINT, ForeignKey('users.id'))

class Comments(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    error_code = Column(SMALLINT)
    text = Column(VARCHAR(100000))
    parent = Column(BIGINT, ForeignKey('comments.id'))
    author = Column(BIGINT, ForeignKey('users.id'))
    post = Column(BIGINT, ForeignKey('posts.id'))

class CommentVotes(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    comment = Column(BIGINT, ForeignKey('comments.id'))
    user = Column(BIGINT, ForeignKey('users.id'))

class Gates(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    name = Column(VARCHAR(128))
    description = Column(VARCHAR(100000))
    url = Column(VARCHAR(32768))

class CommunityGates(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    gate_uuid = Column(UUID)
    gate_domain = Column(VARCHAR(512))
    gate_domain = Column(VARCHAR(512))
    permission_level = Column(SMALLINT)
    community = Column(BIGINT, ForeignKey('communities.id'))

class Bans(db.Model):
    id = Column(BIGINT, primary_key=True)
    uuid = Column(UUID, unique=True)
    creation_time = Column(TIMESTAMP)
    expiration_time = Column(TIMESTAMP)
    user_UUID = Column(UUID)
    user_domain = Column(VARCHAR(512))
    reason  = Column(VARCHAR(100000))
    community = Column(BIGINT, ForeignKey('communities.id'))






