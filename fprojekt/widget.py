from fprojekt.utils import template_render, pool, url_for, local

def user_header():
    from fprojekt.models.user import get_frontpage_data
    userid = local.session.get("user_login", None)
    user_name, = get_frontpage_data(userid)
    
    return template_render("widgets/user_header.mako",
        user_name = user_name
    )

