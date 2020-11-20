import functools
import json
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import cache
from src import cache_layer as cl

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/',methods=('GET',))
def b():
    return 'random'


@bp.route('/post/',methods=('POST',))
def add_post():
    n = cache.dbsize()
    data = request.get_json()
    cache.set(n+1,data["msg"])

    return 'OK'+str(n+1)

@bp.route('/post/<int:postid>/',methods=('GET',))
def get_post(postid):
    return str(cache.get(postid))
