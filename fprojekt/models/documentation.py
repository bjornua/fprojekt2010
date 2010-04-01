from fprojekt.utils import pool


def get_list_by_user(user_id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id, title, time_created, time_modified, 2
        from documentation
        where user_id=%s and deleted=false order by time_modified desc""",
        (user_id,)
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

def get_document(id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select d.id, d.title, d.time_modified, u.name, u.email
        from documentation d, user u
        where
            u.id = d.user_id
        and d.id = %s""",
        (id,)
    )
    try:
        conn.commit()
        return c.fetchone()
    finally:
        c.close()
        pool.give(conn)


def get_document_sections(documentation_id):
    conn = pool.take()
    c = conn.cursor()
    c.execute(
        """select id, title, content
        from documentation_section
        where
            documentation_id=%s
            and deleted=false
        order by `order`""",
        (documentation_id,)
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
