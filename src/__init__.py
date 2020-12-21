from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import click

from flask import redirect

CONFIG_FILE = 'config.json'

db = SQLAlchemy()
cache = FlaskRedis()

def create_app(test_config=None):
    # create and configure the app
    #TODO: Serve static files with nginx
    app = Flask(__name__,
            instance_relative_config=True,
            static_url_path='',
            static_folder='./static',
            template_folder='./templates')
    app.config.from_json(CONFIG_FILE)

    #attach models to db
    from . import database
    db.init_app(app)

    #register init-db cli option
    app.cli.add_command(init_db_command)

    #setup cache
    cache.init_app(app)

    #register api
    from . import api
    app.register_blueprint(api.bp)

    #register main
    from . import main
    app.register_blueprint(main.bp)

    return app

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)
    click.echo('Initialized the database.')
