# -*- coding: utf-8 -*-
from werkzeug import Local, LocalManager, Response
from werkzeug.routing import Map, Rule
from os.path import dirname, join
from mako.lookup import TemplateLookup
from fprojekt.config import config
from fprojekt.lib import pool
import MySQLdb

__all__ = [
    "root_path",
    "local",
    "application",
    "expose",
    "render_template",
    "url_for",
    "config",
    "pool"
]

root_path = dirname(__file__)

# Magic thread container :)
local = Local()
local_manager = LocalManager([local])
application = local("application")

url_map = Map()
def expose(rule, **kw):
    def decorate(f):
        kw["endpoint"] = f.__name__
        url_map.add(Rule(rule, **kw))
        return f
    return decorate

def url_for(endpoint, _external=False, **values):
    return local.url_adapter.build(endpoint, values, force_external=_external)

template_lookup = TemplateLookup(
    directories=[join(root_path, "templates")],
    input_encoding="utf-8",
    output_encoding="utf-8"
)

def template_response(templatename, response, **kwargs):
    from xml.sax.saxutils import quoteattr, escape
    from fprojekt import widget
    import json
    template = template_lookup.get_template(templatename)
    kwargs["response"] = response
    kwargs["url_for"] = url_for
    kwargs["esc_attr"] = quoteattr
    kwargs["escape"] = escape
    kwargs["widget"] = widget
    kwargs["json"] = json.dumps
    response.data = template.render(**kwargs)

def template_render(widgetname, **kwargs):
    from xml.sax.saxutils import quoteattr, escape
    from fprojekt import widget
    import json
    template = template_lookup.get_template(widgetname)
    kwargs["url_for"] = url_for
    kwargs["esc_attr"] = quoteattr
    kwargs["escape"] = escape
    kwargs["widget"] = widget
    kwargs["json"] = json.dumps
    return template.render(**kwargs).decode("utf-8")

pool = pool.Pool(
    creator = lambda: MySQLdb.connect(
        host=config["mysql_address"],
        user=config["mysql_username"],
        passwd=config["mysql_password"],
        db=config["mysql_database"],
        charset="utf8",
        use_unicode=True
    ),
    maxsize=10
)
