import functools
import json
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
def add_post(post_id):
    data = request.get_json()
    data = validate_request(['title','url','text','community'])
    dl.add_post(UserID(),**data)
    data["msg"]
    return 'OK'

@bp.route('/post/<int:post_id>/',methods=('GET','UPDATE',))
def get_post(post_id):
    return jsonify(dl.get_post(UserID(),post_id=post_id))

@bp.route('/post/<int:post_id>/',methods=('GET','UPDATE',))
def update_post(post_id):
    data = validate_request(['title','url','text','community'])
    data['post_id'] = post_id
    dl.update_post(UserID(),**data)
    return 'OK'

#Comments
#------------------------------------------------------------------
@bp.route('/comment/',methods=('POST',))
def add_comment():
    data = validate_request(['text','parent','post'])
    dl.add_comment(UserID(),**data)
    return 'OK'

@bp.route('/comment/<int:comment_id>/',methods=('GET',))
def get_comment(comment_id):
    return jsonify(dl.get_comment(UserID(),comment_id=comment_id))

@bp.route('/comment/<int:comment_id>/',methods=('UPDATE',))
def update_comment(comment_id):
    data = validate_request(['text'])
    dl.update_comment(UserID(),**data)
    return 'OK'

#Communities
#------------------------------------------------------------------
@bp.route('/community/',methods=('GET',))
def get_communities():
    return jsonify(dl.get_communies(UserID()))

@bp.route('/community/',methods=('POST',))
def add_community():
    data = validate_request(['name'])
    dl.add_community(UserID(),**data)
    return 'OK'

@bp.route('/community/<int:community_id>/',methods=('GET',))
def get_community(community_id):
    return jsonify(dl.get_community_settings(UserID(), community_id=community_id))

@bp.route('/community/<int:community_id>/settings/',methods=('GET',))
def get_community_settings(community_id):
   return jsonify(dl.get_community_settings(UserID()))

@bp.route('/community/<int:community_id>/settings/',methods=('UPDATE',))
def update_community_settings():
    data = validate_request(['name'])
    dl.update_community_settings(UserID(),**data)
    return 'OK'

#CommunityGates
#------------------------------------------------------------------
@bp.route('/community/<int:community_id>/gates/',methods=('GET',))
def get_community_gates(community_id):
    return dl.get_community_gates(UserID(),community_id=community_id)

@bp.route('/community/<int:community_id>/gates/',methods=('POST',))
def add_community_gate(community_id):
    data = validate_request(['gate_uuid','gate_domain'])
    data['community_id'] = community_id
    dl.add_community_gate(UserID(), data)
    return 'OK'

@bp.route('/community/<int:community_id>/gates/',methods=('DELETE',))
def remove_community_gate(community_id):
    data = validate_request(['gate_uuid','gate_domain'])
    data['community_id'] = community_id
    dl.remove_community_gate(UserID(), data)
    return 'OK'

#CommunityMods
#------------------------------------------------------------------
@bp.route('/community/<int:community_id>/mods/',methods=('GET',))
def get_community_mods(community_id):
    return jsonify(dl.get_community_mods(UserID(),community_id=community_id))
    
@bp.route('/community/<int:community_id>/mods/',methods=('POST',))
def add_community_mod(community_id):
    data = validate_request(['user_uuid','user_domain','permission_level','rank'])
    data['community_id'] = community_id
    dl.add_community_mods(UserID(),**data)
    return 'OK'

@bp.route('/community/<int:community_id>/mods/',methods=('DELETE',))
def remove_community_mod(community_id):
    data = validate_request(['user_uuid','user_domain'])
    data['community_id'] = community_id
    dl.remove_community_mods(UserID(),**data)
    return 'OK'

#CommunityBans
#------------------------------------------------------------------
@bp.route('/community/<int:community_id>/bans/',methods=('GET',))
def get_bans(community_id):
    return jsonify(dl.get_bans(UserID(),community_id=community_id))

@bp.route('/community/<int:community_id>/bans/',methods=('POST',))
def add_ban(community_id):
    data = validate_request(['user_uuid','user_domain','expiration_time'])
    data['community_id'] = community_id
    dl.ban_community_user(UserID(),**data)
    return 'OK'

@bp.route('/community/<int:community_id>/bans/',methods=('DELETE',))
def revoke_ban(community_id):
    data = validate_request(['user_uuid','user_domain','expiration_time'])
    data['community_id'] = community_id
    dl.unban_community_user(UserID(),**data)
    return 'OK'

#Vote
#------------------------------------------------------------------
@bp.route('/vote/post/<int:post_id>/',methods=('POST',))
def vote_post(post_id):
    data = validate_request(['value'])
    data['post_id'] = post_id
    dl.vote_post(UserID(),post_id)
    return 'OK'

@bp.route('/vote/post/<int:comment_id>/',methods=('POST',))
def vote_comment(comment_id):
    data = validate_request(['value'])
    data['comment_id'] = comment_id
    dl.vote_comment(UserID(),**data)
    return 'OK'

#Gates
#------------------------------------------------------------------
@bp.route("/gate/",methods=('GET',))
def get_gates():
    return jsonify(dl.get_gates())

@bp.route("/gate/",methods=('POST',))
def add_gate():
    data = validate_request(['name','description','url'])
    dl.add_gate(UserID(),data)
    return 'OK'

@bp.route("/gate/<string:gate_uuid>/settings/",methods=('UPDATE',))
def update_gate_settings(gate_uuid):
    data = validate_request(['name','description','url'])
    data['gate_uuid'] = gate_uuid
    dl.update_gate_settings(**data)
    return 'OK'

@bp.route("/gate/<string:gate_uuid>/settings/",methods=('GET',))
def get_gate_settings(gate_uuid):
    return jsonify(dl.get_gate_settings(UserID(),gate_uuid=gate_uuid))

#GateUsers
#------------------------------------------------------------------
@bp.route("/gate/<string:gate_uuid>/",methods=('GET',))
def check_gate(gate_uuid):
    data = validate_request(['user_uuid','user_domain'])
    data['gate_uuid'] = gate_uuid
    response = dl.check_gate(**data)
    return jsonify(response)

@bp.route("/gate/<string:gate_uuid>/",methods=('POST',))
def add_gate_user(gate_uuid):
    data = validate_request(['user_uuid','user_domain'])
    data['gate_uuid'] = gate_uuid
    response = dl.add_gate_user(UserID(),**data)
    return jsonify(response)

@bp.route("/gate/<string:gate_uuid>/",methods=('DELETE',))
def remove_gate_user(gate_uuid):
    data = validate_request(['user_uuid','user_domain'])
    data['gate_uuid'] = gate_uuid
    response = dl.remove_gate_user(UserID(),**data)
    return jsonify(response)

#Authentication
#------------------------------------------------------------------
#TODO: investigate the security of this meme-tier encryption scheme
@bp.route('/pubkey/<string:user_uuid>/')
def get_key(user_uuid):
    return jsonify(dl.get_public_key(user_uuid=user_uuid))

@bp.route('/login/',methods=('POST',))
def login():
    data = validate_request(['username','tag','password'])
    result = dl.login(data)
    if private_key is not None:
        session.clear()
        session['USERNAME'] = username
        session['TAG'] = tag 
        session['UUID'] =  result['uuid']
        session['DOMAIN'] = domain() 
        session['PRIVATE_KEY'] = private_key
        return 'OK'

@bp.route('/logout/',methods=('POST',))
def logout():
    session.clear()
    return 'OK'

@bp.route('/signup/',methods=('POST',))
def signup():
    data = validate_request(['username','tag','password'])
    result = dl.signup(**data)
    return 'OK'
    
@bp.route('/verify/', methods=('GET','POST',))
def verify():
    if request.method == 'GET':
        data = validate_request(['user_uuid','domain'])
        return jsonify(dl.generate_token(**data))
    
    data = validate_request(['username','tag','token','signature'])
    result = dl.validate_token(**data) 
    if result:
        session.clear()
        session['USERNAME'] = data['username'] 
        session['TAG'] = data['tag']
        session['UUID'] = result['uuid']
        session['DOMAIN'] = result['domain']
        return 'OK'

def domain():
    current_app.config['DOMAIN']

def validate_request(fields):
    data = request.get_json()
    for field in fields:
        if field not in data:
            #TODO:Add proper exceptions
            raise Exception
    return data


class UserID():
    def __init__(self):
        self.user_domain = session['uuid']
        self.user_uuid = session['domain']
        self.username = session['user_name']
        self.tag = session['tag']

















