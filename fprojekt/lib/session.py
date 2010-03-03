# -*- coding: utf-8 -*-
from uuid import uuid4
from cPickle import dumps, loads
from fprojekt.utils import pool


import logging
from fprojekt.utils import local

log = logging.getLogger(__name__)

class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self):
        self.request = local.request
        self.uuid = self.request.cookies.get("session")
        self.is_init = False
        self.changed = False
    
    def init(self):
        if self.is_init:
            return
        self.is_init = True
        if self.uuid != None:
            try:
                self.load_session()
                return
            except InvalidCookieException:
                pass
        self.new_session()

    
    def load_session(self):
        conn = pool.take()
        cursor = conn.cursor()
        cursor.execute("select data from session where uuid = %s",(self.uuid,))
        row = cursor.fetchone()
        if row == None:
            raise InvalidCookieException()
        self.data = loads(row[0])
        cursor.close()
        pool.give(conn)
        
    def new_session(self):
        self.uuid = str(uuid4())
        self.data = dict()
        conn = pool.take()
        cursor = conn.cursor()
        cursor.execute(
            "insert into session (uuid, data) VALUES(%s,%s)",
            (self.uuid,dumps(self.data,-1))
        )
        cursor.close()
        conn.commit()
        pool.give(conn)
    
    def save_session(self):
        if not self.changed:
            return
        conn = pool.take()
        cursor = conn.cursor()
        cursor.execute(
            "update session set data=%s where uuid = %s",
            (dumps(self.data,-1), self.uuid)
        )
        cursor.close()
        conn.commit()
        pool.give(conn)
        
    
    def get(self, *args,**kwargs):
        self.init()
        return self.data.get(*args,**kwargs)
    
    def __setitem__(self, *args, **kwargs):
        self.init()
        self.changed = True
        return self.data.__setitem__(*args,**kwargs)
    
    def set_cookie(self, response):
        if self.is_init:
            response.set_cookie("session", self.uuid, max_age=31536000)

