# -*- coding: utf-8 -*-
import logging
from werkzeug import Response, redirect
from fprojekt.utils import expose, template_response, pool, url_for, local
from fprojekt.lib.session import Session


log = logging.getLogger(__name__)

@expose("/")
def index():
    if local.session.get("user_login") != None:
        return redirect(url_for("user_frontpage"))
    if local.session.get("institution_login") != None:
        return redirect(url_for("institution_frontpage"))
    if local.session.get("admin_login") != None:
        return Response("admin")
    response = Response()
    template_response("/pages/frontpage.mako", response)
    return response

@expose("/institution/login")
def institution_login():
    from fprojekt.models.institution import auth
    errors = set()
    if local.request.method == "POST":
        password = local.request.form.get("password", u"")
        local.session["institution_login"] = auth(password)
        if local.session.get("institution_login") != None:
            return redirect(url_for("index"))
        errors.add("auth_fail")
    response = Response()
    template_response("/pages/institution_login.mako", response,
        errors = errors
    )
    return response

@expose("/bruger/login")
def user_login():
    errors = set()
    response = Response()
    email = local.request.form.get("email", "")
    password = local.request.form.get("password", "")
    if local.request.method == "POST":
        from fprojekt.models.user import auth
        local.session["user_login"] = auth(email,password)
        if local.session.get("user_login") != None:
            return redirect(url_for("index"))
        errors.add("auth_fail")
    template_response("/pages/user_login.mako", response,
        email = email,
        errors = errors
    )
    return response

@expose("/administration/login")
def admin_login():
    response = Response()
    template_response("/pages/admin_login.mako", response)
    return response

@expose("/institution")
def institution_frontpage():
    response = Response()
    template_response("/pages/institution_frontpage.mako", response)
    return response

@expose("/administration")
def admin_frontpage():
    response = Response()
    template_response("/pages/admin_frontpage.mako", response)
    return response

@expose("/administration/institution")
def institution_list():
    from fprojekt.models.institution import get_list
    response = Response()
    entries = get_list()
    template_response("/pages/institution_list.mako", response, entries=entries)
    return response

@expose("/administration/institution/opret")
def institution_create():
    from fprojekt.models.institution import add_institution
    from fprojekt.lib.string import validEmail
    input_errors = set()
    name = local.request.form.get("name", u"")
    phone = local.request.form.get("phone", u"")
    email = local.request.form.get("email", u"")
    
    if local.request.method=="POST":
        if(len(name) == 0):
            input_errors.add("name_empty")
        
        if(len(phone) == 0):
            input_errors.add("phone_empty")
        
        if(len(email) == 0):
            input_errors.add("email_empty")
        else:
            if not validEmail(email):
                input_errors.add("email_invalid")
        
        if(len(input_errors) == 0):
            id = add_institution(
                name = name,
                email = email,
                phone = phone
            )
            return redirect(url_for("institution_modify", id=id))

    response = Response()
    template_response("/pages/institution_create.mako", response,
        input_errors = input_errors,
        name = name,
        phone = phone,
        email = email
    )
    return response

@expose("/administration/institution/<int:id>")
def institution_modify(id):
    from fprojekt.models.institution import get_data, update
    from fprojekt.models.user import get_list_by_institution
    from fprojekt.lib.string import validEmail
    response = Response()
    db_name,db_email,db_phone,db_password = get_data(id)
    input_errors = set()
    entries = get_list_by_institution(id)
    
    name = local.request.form.get("name", db_name)
    phone = local.request.form.get("phone", db_phone)
    email = local.request.form.get("email", db_email)
    password = local.request.form.get("password", db_password)
    
    if local.request.method=="POST":
        if(len(name) == 0):
            input_errors.add("name_empty")
        
        if(len(phone) == 0):
            input_errors.add("phone_empty")
        
        if(len(email) == 0):
            input_errors.add("email_empty")

        if(len(password) == 0):
            input_errors.add("password_empty")
        else:
            if not validEmail(email):
                input_errors.add("email_invalid")
        
        if(len(input_errors) == 0):
            update(
                id = id,
                name = name,
                email = email,
                phone = phone,
                password = password
            )
            return redirect(url_for("institution_modify", id=id))

    template_response("/pages/institution_modify.mako", response,
        id = id,
        db_name = db_name,
        db_email = db_email,
        name = name,
        email = email,
        phone = phone,
        password = password,
        entries = entries
    )
    return response

@expose("/administration/institution/<int:id>/slet")
def institution_delete(id):
    from fprojekt.models.institution import id_exists, delete
    response = Response()
    if local.request.method=="POST":
        sure = local.request.form.get("sure") == "yes"
        if sure:
            delete(id)
            response = redirect(url_for("institution_list"))
        else:
            response = redirect(url_for("institution_modify", id=id))
    else:
        template_response("/pages/institution_delete.mako", response,
            id=id
        )
    return response

@expose("/administration/institution/<int:inst_id>/bruger/opret")
def user_create(inst_id):
    from fprojekt.models.user import add_user
    from fprojekt.lib.string import validEmail
    input_errors = set()
    name = local.request.form.get("name", u"")
    email = local.request.form.get("email", u"")
    
    if local.request.method=="POST":
        if(len(name) == 0):
            input_errors.add("name_empty")
        
        if(len(email) == 0):
            input_errors.add("email_empty")
        else:
            if not validEmail(email):
                input_errors.add("email_invalid")
        
        if(len(input_errors) == 0):
            id = add_user(
                name = name,
                email = email,
                inst_id = inst_id,
            )
            return redirect(url_for("user_modify", id=id))

    response = Response()
    template_response("/pages/user_create.mako", response,
        input_errors = input_errors,
        name = name,
        email = email,
        inst_id = inst_id
    )
    return response

@expose("/administration/bruger/<int:id>")
def user_modify(id):
    from fprojekt.models.user import get_data, update, get_instid
    from fprojekt.lib.string import validEmail
    inst_id = get_instid(id)
    response = Response()
    db_name,db_email,db_password = get_data(id)
    input_errors = set()
    name = local.request.form.get("name", db_name)
    email = local.request.form.get("email", db_email)
    password = local.request.form.get("password", db_password)
    
    if local.request.method=="POST":
        if(len(name) == 0):
            input_errors.add("name_empty")
        
        if(len(email) == 0):
            input_errors.add("email_empty")

        if(len(password) == 0):
            input_errors.add("password_empty")
        else:
            if not validEmail(email):
                input_errors.add("email_invalid")
        
        if(len(input_errors) == 0):
            update(
                id = id,
                name = name,
                email = email,
                password = password
            )
            return redirect(url_for("user_modify", id=id))
    
    template_response("/pages/user_modify.mako", response,
        id = id,
        db_name = db_name,
        db_email = db_email,
        name = name,
        email = email,
        password = password,
        inst_id = inst_id
    )
    return response

@expose("/administration/bruger/<int:id>/slet")
def user_delete(id):
    from fprojekt.models.user import id_exists, delete, get_instid
    response = Response()
    inst_id = get_instid(id)
    if local.request.method=="POST":
        sure = local.request.form.get("sure") == "yes"
        if sure:
            delete(id)
            response = redirect(url_for("user_list", inst_id=inst_id))
        else:
            response = redirect(url_for("user_modify", id=id))
    else:
        template_response("/pages/user_delete.mako", response,
            id=id
        )
    return response

def notfound():
    response = Response()
    template_response("/pages/errors/notfound.mako", response)
    return response

def error():
	response = Response()
	template_response("/pages/errors/error.mako", response)
	return response

@expose("/debug")
def session_debug():
    if local.application.debug == False:
        return notfound()
    from pprint import pformat
    local.session.init()
    response = Response(pformat(local.session.data))
    response.mimetype="text/plain"
    response.charset = "utf-8"
    return response

@expose("/bruger")
def user_frontpage():
    response = Response()
    template_response("/pages/user_frontpage.mako", response)
    return response
