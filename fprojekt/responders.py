# -*- coding: utf-8 -*-
import logging
from werkzeug import Response, redirect
from fprojekt.utils import expose, template_response, pool, url_for, local
from fprojekt.lib.session import Session


log = logging.getLogger(__name__)

@expose("/")
@expose("/index")
def frontpage():
    response = Response()
    template_response("/pages/frontpage.mako", response)
    return response

def notfound():
    response = Response()
    template_response("/pages/errors/notfound.mako", response)
    return response

def error():
	response = Response()
	template_response("/pages/errors/error.mako", response)
	return response
