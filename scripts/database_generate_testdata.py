#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path[0] = os.path.join(os.path.dirname(__file__), "..")

import MySQLdb

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

def generate_institutions(connection):
    def generate_mail(name):
        name = name.lower()
        name = name.replace(u"æ", u"ae")
        name = name.replace(u"ø", u"oe")
        name = name.replace(u"å", u"aa")
        name = name.split(u" ")
        name = reduce(lambda x,y: x+y.split(u"."), name,[])
        name = filter(lambda x: len(x)>0, name)
        name = u"-".join(name)
        return name + u"@haderslev.dk"
    def generate_phone():
        from random import randint
        return u"".join([u"+4563"] + [unicode(randint(0,9)) for x in xrange(6)])
    
        
    c = connection.cursor()
    test = [
        u"Brumbassen",u"Bøgely",u"Cathrine Asylet",u"Deutscher Kindergarden",
        u"Ejsbølhus",u"Favrdal",u"Fjelstrup",u"Frk. Michaels",
        u"Gram Børnehave",u"Hammelev",u"Havanna",u"Hoptrup",u"Kastaniegården",
        u"Kastaniehaven",u"Kløverlykke",u"Kridthuset",u"Lærkereden",
        u"Marie Nielsens",u"Marstup",u"Myretuen Bevtoft",u"Myretuen Fole",
        u"Møllebakken",u"Møllehaven",u"Perlen",u"Povlsbjerg",u"Rosengården",
        u"Ryeshave",u"Sct. Georgs Gården",u"Sdr. Otting",u"Skovreden",
        u"Skrydstrup",u"Solstrålen",u"Stevelt Skovbhv",u"Sukkertoppen",
        u"Søndergades bhv",u"Troldehaven",u"Troldemarken",u"Udsigten",
        u"Vedsted",u"Vilstrup",u"Vænget"
    ]
    password = (unicode(x) for x in xrange(len(test))).__iter__()
    test = ((x,generate_mail(x), generate_phone(),password.next()) for x in test)    
    c.executemany("""
        insert into institution(name, email, phone, password, deleted)
         values(%s,%s,%s,%s,false)""", test)
    connection.commit()
    c.close()

def generate_users(connection):
    def generate_mail(name):
        name = name.lower()
        name = name.replace(u"æ", u"ae")
        name = name.replace(u"ø", u"oe")
        name = name.replace(u"å", u"aa")
        name = name.replace(u"ü", u"u")
        name = name.split(u" ")
        name = reduce(lambda x,y: x+y.split(u"."), name,[])
        name = filter(lambda x: len(x)>0, name)
        name = u"-".join(name)
        return name + u"@haderslev.dk"
    c = connection.cursor()
    first_names = [
        u"Marie",u"Peter",u"Christian",u"Erik",u"Anna",u"Jens",u"Hans",
        u"Margrethe",u"Niels",u"Jørgen",u"Karen",u"Kirstine",u"Kristian",
        u"Kirsten",u"Johanne",u"Henrik",u"Poul",u"Elisabeth",u"Svend",u"Søren",
        u"Aage",u"Michael",u"Lars",u"Else",u"Ole",u"Anne",u"Martin",u"Inger",
        u"Anders",u"Mette",u"Thomas",u"Louise",u"Johannes",u"Maria",u"Ellen",
        u"Knud",u"Kristine",u"Hanne",u"Sofie",u"Jan",u"Emil",u"John",u"Inge",
        u"Bent",u"Karl",u"Carl",u"Henning",u"Per",u"Susanne",u"Frederik",
        u"Rasmus",u"Morten",u"Helle",u"Andreas",u"Jesper",u"Grethe",u"Arne",
        u"Marianne",u"Kim",u"Lene",u"Gerda",u"Børge",u"Peder",u"Birthe",
        u"Charlotte",u"Bente",u"Birgit",u"Tove",u"Flemming",u"Edith",u"Ruth",
        u"Kaj",u"Mads",u"Kathrine",u"Pia",u"Lone",u"Christine",u"Camilla",
        u"Emilie",u"Leif",u"Jytte",u"Jette",u"Torben",u"Kurt",u"Birgitte",
        u"Mogens",u"Helene",u"Bodil",u"Julie",u"Steen",u"Jacob",u"Henry",u"Lis",
        u"Ove",u"Katrine",u"Lise",u"Ulla",u"Bjarne",u"Finn",u"Claus",u"Gitte",
        u"Ingeborg",u"Eva",u"Tina",u"Preben",u"Bo",u"Gudrun",u"Irene",u"Otto",
        u"Mikkel",u"Cecilie",u"Allan",u"Carsten",u"Ane",u"Christina",u"Vibeke",
        u"Ingrid",u"Jakob",u"Marius",u"Johan",u"Brian",u"Annette",u"Ida",
        u"Egon",u"Rikke",u"Holger",u"Emma",u"Alfred",u"Laura",u"Mathias",
        u"Viggo",u"Daniel",u"Jonas",u"Simon",u"Karin",u"Valdemar"
    ]
    last_names = [
        u"Nielsen",u"Hansen",u"Pedersen",u"Andersen",u"Christensen",u"Larsen",
        u"Sørensen",u"Rasmussen",u"Petersen",u"Jørgensen",u"Madsen",
        u"Kristensen",u"Olsen",u"Christiansen",u"Thomsen",u"Poulsen",
        u"Johansen",u"Knudsen",u"Mortensen",u"Møller",u"Jacobsen",u"Jakobsen",
        u"Olesen",u"Frederiksen",u"Mikkelsen",u"Henriksen",u"Laursen",u"Lund",
        u"Schmidt",u"Eriksen",u"Holm",u"Kristiansen",u"Clausen",u"Simonsen",
        u"Svendsen",u"Andreasen",u"Iversen",u"Jeppesen",u"Mogensen",
        u"Jespersen",u"Nissen",u"Lauridsen",u"Frandsen",u"Østergaard",
        u"Jepsen",u"Kjær",u"Carlsen",u"Vestergaard",u"Jessen",u"Nørgaard",
        u"Dahl",u"Christoffersen",u"Skov",u"Søndergaard",u"Bertelsen",u"Bruun",
        u"Lassen",u"Bach",u"Gregersen",u"Friis",u"Johnsen",u"Steffensen",
        u"Kjeldsen",u"Bech",u"Krogh",u"Lauritsen",u"Danielsen",u"Mathiesen",
        u"Andresen",u"Brandt",u"Winther",u"Toft",u"Ravn",u"Mathiasen",u"Dam",
        u"Holst",u"Nilsson",u"Lind",u"Berg",u"Schou",u"Overgaard",
        u"Kristoffersen",u"Schultz",u"Klausen",u"Karlsen",u"Paulsen",
        u"Hermansen",u"Thorsen",u"Koch",u"Thygesen",u"Bak",u"Kruse",u"Bang",
        u"Juhl",u"Davidsen",u"Berthelsen",u"Nygaard",u"Lorentzen",u"Villadsen",
        u"Lorenzen",u"Damgaard",u"Bjerregaard",u"Lange",u"Hedegaard",
        u"Bendtsen",u"Lauritzen",u"Svensson",u"Justesen",u"Juul",u"Hald",
        u"Kofoed",u"Søgaard",u"Munk",u"Meyer",u"Kjærgaard",u"Riis",u"Johannsen",
        u"Carstensen",u"Bonde",u"Ibsen",u"Fischer",u"Andersson",u"Bundgaard",
        u"Aagaard",u"Johannesen",u"Eskildsen",u"Hemmingsen",u"Andreassen",
        u"Thomassen",u"Schrøder",u"Persson",u"Hjorth",u"Enevoldsen",u"Nguyen",
        u"Henningsen",u"Jønsson",u"Olsson",u"Asmussen",u"Michelsen",u"Vinther",
        u"Markussen",u"Kragh",u"Thøgersen",u"Johansson",u"Dalsgaard",u"Gade",
        u"Bjerre",u"Ali",u"Laustsen",u"Buch",u"Ludvigsen",u"Hougaard",u"Beck",
        u"Kirkegaard",u"Marcussen",u"Mølgaard",u"Ipsen",u"Sommer",u"Ottosen",
        u"Müller",u"Krog",u"Hoffmann",u"Clemmensen",u"Nikolajsen",u"Brodersen",
        u"Therkildsen",u"Leth",u"Michaelsen",u"Graversen",u"Frost",u"Dalgaard"
    ]
#    print len(first_names)
#    print len(last_names)
#    exit()
    
    def generate_name():
        from random import choice
        return "%s %s" % (choice(first_names),choice(last_names))
    
    c.execute("select id from institution")
    while True:
        insertcursor = connection.cursor()
        row = c.fetchone()
        if row == None:
            break
        (id,) = row
        from random import randint
        from MySQLdb import IntegrityError
        i=0
        for x in xrange(randint(8,17)):
            while True:
                name = generate_name()
                email = generate_mail(name)
                try:
                    insertcursor.execute("""
                        insert into user(name, email, institution_id, password, deleted)
                        values(%s,%s,%s,"1234",false)
                    """, (name,email,id))
                    break
                except IntegrityError:
                    i+=1
    connection.commit()
    insertcursor.close()
    c.close()


if __name__ == "__main__":
    connection = get_connection()
    generate_institutions(connection)
    generate_users(connection)
    
    connection.close()
