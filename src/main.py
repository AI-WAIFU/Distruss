import functools
import json
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src import data_layer as dl


bp = Blueprint('main', __name__, url_prefix='')

@bp.route('/')
def main():
    return redirect(url_for('static',filename='index.html'))


#culture
@bp.route('/kaka')
def kaka():
    return redirect('https://kaka.moe/')

#hello
@bp.route('/hello')
def hello():
    return 'Hello World!'
