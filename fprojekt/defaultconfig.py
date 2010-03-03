__all__ = ["config"]
def config():
    c = dict()
    c["mysql_address"] = "127.0.0.1"
    c["mysql_username"] = ""
    c["mysql_password"] = ""
    c["mysql_database"] = ""
    c["smtp_address"] = "127.0.0.1"
    c["smtp_port"] = 25
    return c
