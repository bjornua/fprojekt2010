#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import dirname, join
from pprint import pformat
import sys
sys.path[0] = join(dirname(__file__), "..")

def user_query(itemname, converter, default=None):
    while True:
        if default == None:
            answer = raw_input("Indtast %s: " % (itemname,))
        else:
            answer = raw_input("Indtast %s [%s]: " % (itemname, default))
            if answer == "":
                return default
        try:
            answer = converter(answer)
        except:
            print "Kunne ikke forstå værdien, prøv igen."
            continue
        return answer

def prompt_update_config():
    try:
        from fprojekt.config import config
    except ImportError:
        from fprojekt.defaultconfig import config
        config = config()

    for name, key, converter in [
        ("MySQL Adresse"    , "mysql_address" , str),
        ("MySQL Brugernavn" , "mysql_username", str),
        ("MySQL Adgangskode", "mysql_password", str),
        ("MySQL Database"   , "mysql_database", str),
        ("SMTP Adresse"     , "smtp_address"  , str),
        ("SMTP Port"        , "smtp_port"     , int)
    ]:
        config[key] = user_query(name, converter, config[key])
    return config

def write_config(config):
    filename = join(dirname(__file__), "..", "fprojekt", "config.py")
    fhandle = open(filename, "w")
    fhandle.write(
        "from fprojekt.defaultconfig import config\n"
      + "config = config()\n"
      + "config.update(\n"
      + pformat(config, indent=4) + "\n"
      + ")"
    )

if __name__ == "__main__":
    config = prompt_update_config()
    write_config(config)
