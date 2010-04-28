# -*- coding: utf-8 -*-
import logging
from werkzeug import Response, redirect
from fprojekt.utils import expose, template_response, pool, url_for, local
from fprojekt.lib.session import Session
from fprojekt.models import user, institution, admin, documentation
log = logging.getLogger(__name__)

@expose("/")
def index():
    if user.is_authed():
        return redirect(url_for("user_frontpage"))
    if institution.is_authed():
        return redirect(url_for("institution_frontpage"))
    if admin.is_authed():
        return Response("admin")
    response = Response()
    template_response("/pages/frontpage.mako", response)
    return response

@expose("/institution")
def institution_frontpage():
    response = Response()
    
    if not institution.is_authed():
        return redirect(url_for("index"))

    id = institution.get_session_institution_id()
    name = institution.get_name(id)
    users = user.get_inst_login_users(id)
    template_response("/pages/institution_frontpage.mako", response,
        name = name,
        users = users
    )
    return response

@expose("/institution/login")
def institution_login():
    errors = set()
    if local.request.method == "POST":
        password = local.request.form.get("password", u"")
        is_authed = institution.login(password)
        if is_authed:
            return redirect(url_for("index"))
        errors.add("auth_fail")
    response = Response()
    template_response("/pages/institution_login.mako", response,
        errors = errors
    )
    return response
@expose("/institution/logout")
def institution_logout():
    institution.logout()
    return redirect (url_for("index"))

@expose("/bruger")
def user_frontpage():
    from fprojekt.models.documentation import get_list_by_user
    from fprojekt.models.user import is_authed, get_session_user_id, get_frontpage_data
    response = Response()
    
    if not is_authed():
        return redirect(url_for("index"))
    
    userid = get_session_user_id()
    username, = get_frontpage_data(userid)
    documents = get_list_by_user(userid)
    
    template_response("/pages/user_frontpage.mako", response,
        username = username,
        documents = documents
    )
    return response

@expose("/bruger/login")
@expose("/bruger/login/<string:email>")
def user_login(email=""):
    errors = set()
    response = Response()
    email = local.request.form.get("email", email)
    password = local.request.form.get("password", "")
    if local.request.method == "POST":
        is_authed = user.login(email,password)
        if is_authed:
            return redirect(url_for("index"))
        errors.add("auth_fail")
    template_response("/pages/user_login.mako", response,
        email = email,
        errors = errors
    )
    return response

@expose("/bruger/logout")
def user_logout():
    user.logout()
    return redirect (url_for("index"))

@expose("/bruger/profil/<int:id>")
def user_profile(id):
    from fprojekt.lib.string import validEmail
    response = Response()
    authed_user = user.get_session_user_id()==id
    input_errors = set()
    
    if authed_user: # Viewing own profile (Possible to change data)
        db_name, db_email, db_password = user.get_data(id)
        name = local.request.form.get("name", db_name)
        email = local.request.form.get("email", db_email)
        new_password = local.request.form.get("new_password", u"")
        new_password_repeat = local.request.form.get("new_password_repeat", u"")
    else:
        db_name, db_email, name, email = "", "", "", ""
        input_errors.add("not_authorized")

    if local.request.method=="POST":
        if(len(email) == 0):
            input_errors.add("email_empty")
        else:
            if not validEmail(email):
                input_errors.add("email_invalid")            
        if(len(new_password) > 0):
            if(new_password_repeat != new_password):
                input_errors.add("passwords_not_the_same")

        if(len(input_errors) == 0 and authed_user):
            # update email NOT password
            user.update(
                id = id,
                name = name,
                email = email,
                password = db_password
            )
            if(len(new_password) > 0):
                # update all settings
                user.update(
                    id = id,
                    name = name,
                    email = email,
                    password = new_password
                )

    template_response("/pages/user_profile_edit.mako", response,
        input_errors = input_errors,
        id = id,
        db_name = db_name,
        db_email = db_email,
        name = name,
        email = email
    )
    return response    

@expose("/administration")
def admin_frontpage():
    response = Response()
    template_response("/pages/admin_frontpage.mako", response)
    return response

@expose("/administration/login")
def admin_login():
    response = Response()
    template_response("/pages/admin_login.mako", response)
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
            response = redirect(url_for("institution_modify", id=inst_id))
        else:
            response = redirect(url_for("user_modify", id=id))
    else:
        template_response("/pages/user_delete.mako", response,
            id=id
        )
    return response

@expose("/dokumentation/print/<int:id>")
def documentation_print(id):
    response = Response()
    from fprojekt.models.documentation import get_document, get_document_sections
    
    document = get_document(id)
    if document == None:
        return notfound()
    
    (doc_id, doc_title, doc_modified, user_name, user_email) = document
    document_sections = get_document_sections(doc_id)
    
    template_response("/pages/document_print.mako", response,
        document_id = doc_id,
        document_title = doc_title,
        document_modified = doc_modified,
        user_name = user_name,
        user_email = user_email,
        document_sections = document_sections
    )
    return response

@expose("/dokumentation/ret/<int:id>")
def documentation_edit(id):
    response = Response()
    from fprojekt.models.documentation import get_document, get_document_sections
    
    document = get_document(id)
    if document == None:
        return notfound()
    
    (doc_id, doc_title, doc_modified, user_name, user_email) = document
    document_sections = get_document_sections(doc_id)
    
    template_response("/pages/document_edit.mako", response,
        document_id = doc_id,
        document_title = doc_title,
        document_modified = doc_modified,
        user_name = user_name,
        user_email = user_email,
        document_sections = document_sections
    )
    return response


@expose("/dokumentation/gem")
def document_save():
    response = Response()
    from fprojekt.models.documentation import update_section
    import json
    section_json = local.request.form.get("section")
    section = json.loads(section_json)
    id = section["id"]
    title = section["title"]
    content = section["content"]
    update_section(id, title, content)
    return response

def notfound():
    response = Response()
    template_response("/pages/errors/notfound.mako", response)
    return response

def error():
	response = Response()
	template_response("/pages/errors/error.mako", response)
	return response

@expose("/vis/billede/<int:id>")
def show_image(id):
    response = Response(user.get_image(id))
    response.mimetype="image/jpeg"
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

@expose("/laereplan")
def curriculum_frontpage():
    response = Response()
    template_response("/pages/curriculum_frontpage.mako", response)
    return response


@expose("/evaluering")
def evaluation_frontpage():
    response = Response()
    template_response("/pages/evaluation_frontpage.mako", response)
    return response
