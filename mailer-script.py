#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import MySQLdb
from fprojekt.config import config
from datetime import datetime

connection_mysql = MySQLdb.connect(
    host=config["mysql_address"],
    user=config["mysql_username"],
    passwd=config["mysql_password"],
    db=config["mysql_database"],
    charset="utf8",
    use_unicode=True
)
connection_smtp = smtplib.SMTP(
    host=config["smtp_address"],
    port=config["smtp_port"]
)

def get_id():
    c = connection_mysql.cursor()
    c.execute("select id from outgoing_mail where processed is null limit 1")
    try:
        return c.fetchone()[0]
    except TypeError:
        return None
    finally:
        c.close()

def notify_processing(id):
    c = connection_mysql.cursor()
    try:
        # True if we are the only one processing this mail.
        # False if another process beat us to it.
        return 1 == c.execute("""
                update outgoing_mail
                set processed = %s
                where
                    processed is null
                    and id=%s
            """, (datetime.now(), id)
        )
    finally:
        connection_mysql.commit()
        c.close()

def get_mail(id):
    c = connection_mysql.cursor()
    try:
        c.execute("""
                select sender, recipient, content
                from outgoing_mail
                where id=%s
            """, (id,)
        )
        return c.fetchone()
    finally:
        c.close()

while True:
    id = get_id()
    if id == None:
        break
    if not notify_processing(id):
        continue
    sender,recipient, content = get_mail(id)
    connection_smtp.sendmail(sender,recipient, content)
