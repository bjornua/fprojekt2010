#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path[0] = os.path.join(os.path.dirname(__file__), "..")


import MySQLdb
from pprint import pprint

class ConfigException(Exception): pass
def get_connection():
    try:
        from fprojekt.config import config
    except ImportError:
        raise ConfigException("Please configure first.")
    return MySQLdb.connect(
            host=config["mysql_address"],
            user=config["mysql_username"],
            passwd=config["mysql_password"],
            db=config["mysql_database"]
    )

def drop_tables(connection):
    c = connection.cursor()
    
    c.execute("drop table if exists `documentation_section`")
    c.execute("drop table if exists `documentation`")
    c.execute("drop table if exists `outgoing_mail`")
    c.execute("drop table if exists `user_has_privilege`")
    c.execute("drop table if exists `user`")
    c.execute("drop table if exists `institution`")
    c.execute("drop table if exists `session`")
    c.close()
    
def create_tables(connection):
    c = connection.cursor()
    c.execute("""
        create table `session` (
            `uuid` char(36) not null,
            `data` blob not null,
            primary key (`uuid`)
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
        """)
    c.execute("""
        create table `institution` (
            `id` int unsigned not null auto_increment,
            `name` varchar(255) not null,
            `email` varchar(255) default null,
            `phone` varchar(255) default null,
            `password` varchar(32) default null,
            `deleted` bool default false,
            primary key (`id`),
            index `deleted` (`deleted`),
            unique `auth` (`deleted`,`password`(4)),
            index `lookup` (`deleted`,`id`)
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.execute("""
        create table `user` (
            `id` int unsigned not null auto_increment,
            `email` varchar(255) not null,
            `password` varchar(255) not null,
            `name` varchar(255) default null,
            `institution_id` int unsigned default null,
            `deleted` bool default false,
            `image` BLOB,
            primary key (`id`),
            unique `email` (`email`),
            index `auth` (deleted,`email`(10),`password`(10)),
            index `name` (`name`(10)),
            constraint `institution_id` foreign key (`institution_id`) references `institution` (`id`)
                on delete cascade
                on update cascade
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.execute("""
        create table `user_has_privilege` (
            `user_id` int unsigned not null,
            `privilege_id` int unsigned not null,
            primary key (`user_id`,`privilege_id`),
            constraint `user_has_privilege` foreign key (`user_id`) references `user` (`id`)
                on delete cascade
                on update cascade
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.execute("""
        create table `outgoing_mail` (
            `id` int unsigned not null auto_increment,    
            `processed` datetime default null,
            `sender` varchar(255) CHARACTER SET ascii not null,
            `recipient` varchar(255) CHARACTER SET ascii not null,
            `content` text CHARACTER SET ascii not null,
            `error_message` text default null,
            primary key (`id`),
            key `processed`(`processed`)
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.execute("""
        create table `documentation` (
            `id` int unsigned not null auto_increment,    
            `title` varchar(255) not null,
            `time_created` datetime not null,
            `time_modified` datetime not null,
            `user_id` int unsigned not null,
            `deleted` bool not null,
            primary key (`id`),
            index `user_id`(`user_id`),
            constraint `user_has_doc` foreign key (`user_id`) references `user` (`id`)
                on delete cascade
                on update cascade
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.execute("""
        create table `documentation_section` (
            `id` int unsigned not null auto_increment,    
            `title` varchar(255) not null,
            `content` text not null,
            `order` int unsigned not null,
            `documentation_id` int unsigned not null,
            `deleted` bool not null,
            primary key (`id`),
            index `order`(`order`),
            constraint `documentation` foreign key (`documentation_id`) references `documentation` (`id`)
                on delete cascade
                on update cascade
        )
        engine=InnoDB
        default charset=utf8
        collate=utf8_danish_ci
        pack_keys=1
    """)
    c.close()

if __name__ == "__main__":
    connection = get_connection()
    drop_tables(connection)
    create_tables(connection)
    connection.close()
