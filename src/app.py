import time

import psycopg2
import redis

from flask import Flask
from flask import current_app, g
from flask.cli import with_appcontext 

DB_STRING = "host=database port=5433 dbname=yugabyte user=yugabyte password=yugabyte";

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Fuck! I have been seen {} times.\n'.format(count)

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(DB_STRING)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

