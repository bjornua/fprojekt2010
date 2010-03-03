#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cherrypy import wsgiserver
from fprojekt.application import Application

app = Application(debug=False)

server = wsgiserver.CherryPyWSGIServer(("0.0.0.0", 5000), app)
try:
    server.start()
except KeyboardInterrupt:
    server.stop()
