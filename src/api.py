import functools
import json
import jsonschema
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
)

from src import data_layer as dl

bp = Blueprint('api', __name__, url_prefix='/api')

#API schema
#------------------------------------------------------------------
@bp.route('/',methods=('GET',))
def schema():
    #TODO: Make this return an actual schema or configure reverse
    #proxy to do it
    return jsonify(dl.get_schema())

#Federation Directory
#------------------------------------------------------------------
@bp.route('/directory/',methods=('GET',))
def directory():
    return jsonify(dl.get_directory())

#Posts
#------------------------------------------------------------------
@bp.route('/post/',methods=('POST',))
def add_post():
    data = request.get_json()
    data["msg"]

    return 'OK'

@bp.route('/post/<int:postid>/',methods=('GET','UPDATE',))
def get_post(postid):
    return str(cache.get(postid))

#Comments
#------------------------------------------------------------------
@bp.route('/comment/',methods=('POST',))
def add_comment():
    data = request.get_json()

    return 'OK'

@bp.route('/comment/<int:commentid>/',methods=('GET',))
def get_comment(commentid):
    data = request.get_json()

    return jsonify()

@bp.route('/comment/<int:commentid>/',methods=('UPDATE',))
def update_comment(commentid)):
    data = request.get_json()

    return 'OK'

#Communities
#------------------------------------------------------------------
@bp.route('/community/',methods=('POST',))
def add_community():
    data = request.get_json()

    return 'OK'

@bp.route('/community/int:communityid>/',methods=('GET',))
def get_community(communityid):
    data = request.get_json()

    return jsonify()


@bp.route('/community/<int:communityid>/settings/',methods=('GET','UPDATE'))
def community_settings(communityid):
    data = request.get_json()

    return 'OK'

#Vote
#------------------------------------------------------------------
@bp.route('/vote/post/<int:postid>/',methods=('POST',))
def vote_post():
    data = request.get_json()

    return 'OK'

@bp.route('/vote/post/<int:commentid>/',methods=('POST',))
def vote_comment():
    data = request.get_json()

    return 'OK'

#Gates
#------------------------------------------------------------------
@bp.route("/gate/",methods=('POST',))
def add_gate():
    data = request.get_json()
    dl.add_gate()
    return 'OK'

@bp.route("/gate/<string:gate_uuid>/",methods=('GET'))
def get_gate(gate_uuid):
    return jsonify(dl.get_gate(gate_uuid))

@bp.route("/gate/<string:gate_uuid>/settings/",methods=('GET','UPDATE'))
def gate_settings(gate_uuid):
    if request.method == 'UPDATE':
        data = request.get_json()
        name = data['name']
        description = data['description']
        url = data['url']
        dl.update_gate_settings(gate_uuid, name, description, url)
        return 'OK'
    else:
        return jsonify(dl.get_gate_settings(gate_))


@bp.route("/gate/",methods=('GET',))
def check_gate()
    data = request.get_json()
    user_uuid  = data['user_uuid']
    user_domain = data['user_domain']
    response = dl.check_gate(user_uuid,user_domain)
    return jsonify(response)


#Authentication
#------------------------------------------------------------------
@bp.route('/pubkey/<string:user_uuid>/')
def get_key(user_uuid):
    return jsonify(dl.get_public_key(userid))

@bp.route('/login',methods=('POST',))
def login():
    data = request.get_json()
    username = data['username']
    tag = data['tag']
    password = data['password']
    
    #TODO: investigate the security of this meme-tier encryption scheme
    private_key = dl.login(username, tag, password)
    if private_key is not None:
        session.clear()
        session['USERNAME'] = username
        session['TAG'] = tag 
        session['PRIVATE_KEY'] = private_key
    return 'OK'
    

@bp.route('/logout',methods=('POST',))
def logout():
    session.clear()
    return 'OK'

@bp.route('/signup',methods=('POST',))
def signup():
    data = request.get_json()
    username = data['username']
    tag = data['tag']
    password = data['password']
    email = data['email']
    phone = data['phone']
    dl.signup(username, tag, password, email, phone)
    return 'OK'
    



















