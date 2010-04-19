from fprojekt.utils import local



def is_authed():
    return local.session.get("login_administrator") != None
def get_session_admin_id():
    return local.session.get("login_administrator")

