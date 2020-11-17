from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import click

CONFIG_FILE = 'config.json'

db = SQLAlchemy()
cache = FlaskRedis()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_json(CONFIG_FILE)

    #attach models to db
    from . import database
    db.init_app(app)
    cache.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    app = create_app()
    db.drop_all(app=create_app())
    db.create_all(app=create_app())
    click.echo('Initialized the database.')
