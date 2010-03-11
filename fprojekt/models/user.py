from fprojekt.utils import pool
from random import sample

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def _generate_password():
    password = "".join(sample(characters,16))
    return password

def auth(email,password):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id
        from user where email=%s and password=%s and deleted=false""",
        (email,password)
    )
    conn.commit()
    try:
        return c.fetchone()[0]
    except TypeError:
        return None
    finally:
        c.close()
        pool.give(conn)

def get_list_by_institution(inst_id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id, name, email
        from user
        where institution_id=%s and deleted=false""",
        (inst_id,)
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
    

def add_user(name, email, inst_id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """insert into user (name, email, password, institution_id)
        values(%s,%s,%s,%s)""",
        (name, email, _generate_password(), inst_id)
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
        """select name, email, password
        from user where id = %s and deleted=false""",
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
        """select 1 from user where deleted=false and id=%s""",
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
        """update user set deleted=true where id=%s""",
        (id,)
    )
    conn.commit()
    c.close()
    pool.give(conn)

def update(id, name, email, password):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """update user set name=%s, email=%s, password=%s
        where id=%s and deleted=false""",
        (name, email, password, id)
    )
    conn.commit()
    c.close()
    pool.give(conn)


def get_instid(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select institution_id
        from user where id = %s""",
        (id,)
    )
    conn.commit()
    try:
        return c.fetchone()[0]
    finally:
        c.close()
        pool.give(conn)

