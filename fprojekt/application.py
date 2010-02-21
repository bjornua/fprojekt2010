# -*- coding: utf-8 -*-
from werkzeug import Request, Response


class Application(object):
    def __init__(self):
        pass
    
    def dispatch(self, environ, start_response):
        request = Request(environ)
        response = Response("Test")
        return response(environ, start_response)
    
    def __call__(self, environ, start_response):
        return self.dispatch(environ, start_response)       
