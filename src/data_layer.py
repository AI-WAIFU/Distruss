from . import cache
from . import db

#API schema
#------------------------------------------------------------------
def get_schema():
    pass

#Federation Directory
#------------------------------------------------------------------
def get_directory():
    pass

#Posts
#------------------------------------------------------------------
def add_post(user_id, title=None, url=None, text=None, community=None):
    pass

def get_post(user_id, post_id=None):
    pass

def update_post(user_id, post_id=None, title=None, url=None, text=None, community=None):
    pass

#Comments
#------------------------------------------------------------------
def add_comment(user_id, text=None, parent=None, post=None):
    pass

def get_comment(user_id, comment_id=None):
    pass

def update_comment(user_id, comment_id=None, text=None):
    pass

#Communities
#------------------------------------------------------------------
def get_communities(user_id):
    pass

def add_community(user_id, name=None):
    pass

def get_communities(user_id, community_id=None):
    pass

def get_community_settings(user_id, community_id=None):
    pass

def update_community_settings(user_id, community_id=None, name=None):
    pass


#CommunityGates
#------------------------------------------------------------------
def get_community_gates(user_id, community_id=None):
    pass

def add_community_gate(user_id, community_id=None, gate_uuid=None, gate_domain=None):
    pass

def remove_community_gate(user_id, community_id=None, gate_uuid=None, gate_domain=None):
    pass

#CommunityMods
#------------------------------------------------------------------
def get_community_mods(user_id, community_id=None):
    pass

def add_community_mod(user_id, community_id=None, user_uuid=None, user_domain=None, permission_level=None, rank=None):
    pass

def remove_community_mod(user_id, community_id=None, user_uuid=None, user_domain=None):
    pass

#CommunityBans
#------------------------------------------------------------------
def get_bans(user_id, community_id=None):
    pass 

def add_ban(user_id, community_id=None, user_uuid=None, user_domain=None, expiration_time=None):
    pass 

def revoke_ban(user_id, community_id=None, user_uuid=None, user_domain=None):
    pass 

#Vote
#------------------------------------------------------------------
def vote_post(user_id, post_id=None):
    pass

def vote_comment(user_id, comment_id=None):
    pass

#Gates
#------------------------------------------------------------------
def get_gates():
    pass

def add_gate(user_id, name=None ,description=None, url=None):
    pass

def update_gate_settings(user_id , gate_uuid=None, name=None ,description=None, url=None):
    pass

def get_gate_settings(user_id, gate_uuid=None):
    pass

#GateUsers
#------------------------------------------------------------------
def check_gates(user_id, gate_uuid=None, user_uuid=None, user_domain=None):
    pass

def add_gate_user(user_id, gate_uuid=None, user_uuid=None, user_domain=None):
    pass

def remove_gate_user(user_id, gate_uuid=None, user_uuid=None, user_domain=None):
    pass

#Authentication
#------------------------------------------------------------------
def get_key(user_uuid=None):
    pass

def login(user_name=None, tag=None, password=None):
    pass

def signup(user_name=None, tag=None, password=None):
    pass

def gen_token(user_uuid=None, user_domain=None):
    pass

def generate_token(user_uuid=None, user_domain=None):
    pass

def validate_token(username=None, tag=None, token=None, signature=None):
    pass
