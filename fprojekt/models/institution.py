# -*- coding: utf-8 -*-
from fprojekt.utils import pool, local
from random import sample

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def _generate_password():
    password = "".join(sample(characters,16))
    return password

def add_institution(name, email, phone):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """insert into institution (name, email, phone, password)
        values(%s,%s,%s,%s)""",
        (name, email, phone, _generate_password())
    )
    id = conn.insert_id()
    conn.commit()
    c.close()
    pool.give(conn)
    return id

def get_data(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select name, email, phone, password
        from institution where id = %s and deleted=false""",
        (id,)
    )
    conn.commit()
    try:
        return c.fetchone()
    finally:
        c.close()
        pool.give(conn)


def get_list():
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id, name, email, phone from institution where deleted=false"""
    )
    conn.commit()
    try:
        while True:
            row = c.fetchone()
            if row == None:
                break
            yield row
    finally:
        c.close()
        pool.give(conn)

def id_exists(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select 1 from institution where deleted=false and id=%s""",
        (id,)
    )
    conn.commit()
    try:
        return c.fetchone != None
    finally:
        c.close()
        pool.give(conn)

def delete(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """update institution set deleted=true where id=%s""",
        (id,)
    )
    conn.commit()
    c.close()
    pool.give(conn)

def update(id, name, email, phone, password):
    conn = pool.take()
    c = conn.cursor()
    try:
        c.execute(
            """update institution set name=%s, email=%s, phone=%s, password=%s
            where id=%s and deleted=false""",
            (name, email, phone, password, id)
        )
    finally:
        conn.commit()
        c.close()
        pool.give(conn)
    
def login(password):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id
        from institution where password = %s and deleted=false""",
        (password,)
    )
    conn.commit()
    row = c.fetchone()
    c.close()
    pool.give(conn)
    if row == None:
        return False
    (id,) = row
    local.session["login_institution"] = id
    return True

def get_name(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select name
        from institution where id = %s and deleted=false""",
        (id,)
    )
    conn.commit()
    try:
        return c.fetchone()[0]
    finally:
        c.close()
        pool.give(conn)

def get_users(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id, name, email, phone from institution where deleted=false"""
    )
    conn.commit()
    try:
        while True:
            row = c.fetchone()
            if row == None:
                break
            yield row
    finally:
        c.close()
        pool.give(conn)
    


def logout():
    local.session["login_institution"] = None
def is_authed():
    return local.session.get("login_institution") != None
def get_session_institution_id():
    return local.session.get("login_institution")

        
    
    

