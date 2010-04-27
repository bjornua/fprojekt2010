from fprojekt.utils import template_render, pool, url_for, local
from fprojekt.models.user import get_session_user_id

def user_header():
    from fprojekt.models.user import get_frontpage_data
    userid = get_session_user_id()
    user_name, = get_frontpage_data(userid)
    
    return template_render("widgets/user_header.mako",
        user_name = user_name
    )

def topmenu(active_section):
    return template_render("widgets/topmenu.mako",
        active_section = active_section
    )

