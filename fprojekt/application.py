# -*- coding: utf-8 -*-
from .lib.session import Session
from .utils import local, url_map
from .werkzeug import Request, Response
from .werkzeug.exceptions import NotFound

class Application(object):
    def __init__(self, debug):
        from os.path import join
        from werkzeug import SharedDataMiddleware
        from .utils import root_path
        
        local.application = self
        self.debug = debug
        self.dispatch = SharedDataMiddleware(self.dispatch, {
                "/static": join(root_path, "static")
            }
        )

    def dispatch(self, environ, start_response):
        from . import responders
        notfound = responders.notfound
        try:
            local.url_adapter = url_adapter = url_map.bind_to_environ(environ)
            local.request = Request(environ)
            local.session = session = Session()
            try:
                endpoint, params = url_adapter.match()
                response = getattr(responders,endpoint)(**params)
            except NotFound:
                response = notfound()
            session.set_cookie(response)
            session.save_session()
        except:
            if self.debug:
                raise
            else:
                try:
                    response = responders.error()
                except:
                    response = Response("Fejlsidens fejlside.")
        return response(environ, start_response)        
    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
