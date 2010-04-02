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
         values(%s, %s, %s, %s, false)""", test)
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
                        values(%s, %s, %s, "1234", false)
                    """, (name,email,id))
                    break
                except IntegrityError:
                    i+=1
    connection.commit()
    insertcursor.close()
    c.close()

def generate_documents(connection):
    from datetime import datetime
    from random import randint
    c = connection.cursor()

    c.execute("select id from user")
    while True:
        insertcursor = connection.cursor()
        row = c.fetchone()
        if row == None:
            break
        (id,) = row
        for x in xrange(randint(1,13)):
            # Random date between 2000/1/1'ish and 2010/1/1'ish
            timestamp = randint(946706400,1262325600)
            created = datetime.utcfromtimestamp(timestamp)
            modified = datetime.utcfromtimestamp(timestamp + randint(0,7776000))
            title = "Unavngivet dokument %d" % x
            
            insertcursor.execute("""
                insert into documentation(title, time_created, time_modified, user_id, deleted)
                values(%s, %s, %s, %s, false)
            """, (title, created, modified, id))
        insertcursor.close()
    connection.commit()
    c.close()

def generate_document_sections(connection):
    c = connection.cursor()
    random_paragraphs = [
    u"""
     <p>Også fugl ud sig, alt man rejste ligesom eller dig nu. Vandet på ned
        frygtelig i så hvem, sukkede hvor sørgmodighed hen dig velopdragen kom,
        de derude så vi, vildgasserne så mennesker. I på. Mod trægrenene, køn
        prøve, rød korn og og skræppeblad rappede din, stå fugle ikke hund
        inderligt med. Fy være være dem sivene hugges, stakkels så og vinger
        øjnede, blev så vildsomt sprog det og lød. Den alle nu frem, siv ham,
        tør solskinnet det bare den, eller den sider ja andre hen jeg, af gik
        prøvet ud. Klask tæt når, i drive ned for få være forfærdelig, syntes
        skvulpede han dig solen skal, ja med den ager. Mening engang venner er,
        de morsomt, nævne skarn, så højt og på går, fange straks styg i de
        genvordighed. Gjorde de flere af din borte har, ganske der hvad jer er
        hang, ganske lykke, ned tålt. Noget stygge ælling ham en set. Isen
        dyrene i om i godt sig, bruger kone der der, troede skreg så
        forunderlig, den med, og sprang.</p>
    """,
    u"""
     <p>Ham sætter, solen stå og hovedet ingen forunderligt man, have spørg nå.
        Men hugge megen skarpe nå der, sig så, og ikke igen at. Verden strakte
        langt er tror af, endnu sagde i, ham boede hønsene, moder havde længe
        i over vi dejligt. ællingemoderen første blive stor ud, ned hun igen
        ikke. Og så af men læg. Ind dit, ganske end, kender med og i fra.
        Drømte og sønnike men, klare ret høet til grønne, skreg snakkede
        vandet kunne at, ved op åben flød i vandet, den imod du ene. Ud
        skaber om, den stuen men ænder, spinde sige troede for, sagde
        dyr natten da. Slog der glemme og, er så spørg børn bens så,
        hvem dukkede aldrig forårsfriskt ællingen de ælling. Sig sang.</p>
     """,
    u"""
     <p>Vi det, grimme have blade hang stille stor, ville i den under. Visit sin
        bringe også, i har, han de, knaldede i, klask noget de fy den jeg. Omgås
        hilste, ikke lad det ville han kunne, rap dyr. Den lukkede
        forskrækkelse, gjorde kom kaldtes ikke lidt være ham. Svømme med og,
        kom da sig forfulgt. Er dage mørke højt og og, den de andre største
        isen, imellem på op over styg det bondehus, dog sammen, moder løb
        forskrækkelse. Om dog, højt du og hang den en ikke, han til dog fælt,
        af æg nød han jer andre hugge. Til den sorrigfuld og ud den grimme,
        aldrig den og løb stakkels. Og spurgte nu andre kommet, smukkeste moder,
        men stor og for var. Sammen sammen for, på fartøj luft er den, konen
        ægget der var i var var, og var har i hvad var. Han præsentere godt ny
        at, bruste sted skvulpede kone.</p>
    """,
    u"""
     <p>Sagde vil af bondehus skarer holde. Anderledes truget du må, ham ligner
        ålehoved at på tage små, og at at, ælling det du smukke sige. Fornemste
        men er bondehus rød, er side, i tålte vil ællingen se lå ligget. Flyve
        tror ganske snart susede sparke vejret. Og og, katten og hagl pillede
        sammen, høet sporer grimhed, av med, sagde kone sige som svaner. Så
        alligevel smallere var ene til af, og sagde skinnede igennem. Du så,
        lærkerne var, hvad har den den, hen de lyst.</p>
    """,
    u"""
     <p>Ikke kan knagede mennesker så, hvor i hagl desuden samme da et, visit en
        vi at. Eller sagde skinnede har dukke, så så en, sig jer med ønske nød
        fordi, sit en stod i så støj som. Den midt lærkerne man man al mig.
        Nåede bruger vi bruger en i. Gik så onde og er, så den knagede skræpper
        op, lige elendigt to dog der så. Stor ned at, og bag for, oh det den
        kan. Men blå konen, ikke godt råbte. ællingen dårligt verden vandet flød
        kom. Dyr lidt kommet og ikke. Den og kan. For altid, ligge har kom til
        grøn støj, han grenene dyr i.</p>
    """,
    u"""
     <p>De af stå jeg, lå styg du og og, dem ønske den ned med at grunden. Den
        og så hun, kunne han dem sine tale, og ænderne den, and på revne at ikke
        at. Kan igen sig, klask moder hang sig ud er, så han så, hønen rejse
        forfulgt ællinger jeg. I din, sagde halsen. Glemme i så dejligt, verden
        al faldt, sprang klare hen den noget. Til agt det, den fra var den. Stor
        på, hugge i blevet meget, fattigt kold hænderne til hjem at med, så
        lykkelige hals under. Bed hvor, rød nåede hvor madamme noget, og ikke
        for sivene stakkels store. Inderligt fra til det imod blev ene, røg en
        ænderne, levende nøfles grimme ælling, sagde styg godt.</p>
    """,
    u"""
     <p>De de med ned jo til derfor, skævt altid, ned katten dykke over se det.
        Lidt her dens det blev kom ja, og siden hårene selv, og mosen løb.
        Forhånet alle ud den, sagde den lige jeg finder den, snakkede på dejligt
        nu andegården, aldrig den ser og i at ville, de stryge glad vide skarpe
        kom. Det ænderne og ham mosen han, så omkring skræppeblad nå tør svømme
        det. Hed og gjorde mange fløj, de andre holde end i, han gult det vi.
        Lærkerne der ville nogen, imod end, vandet ud den i hvad betaget af, er
        være i godt hang brusende hønen, som fik du snart små to har. Ikke hun
        på, tunge hørte kom, vil sagde ind. På før der end, skræppeblade foran
        sider søde vel, stor er efter. Vokser egne, ganske kalkunske er stakkels
        kom godt, her sammen andet sagde mens åben ude. Se af, en den. Gør
        billede at og et fugle, ællingemoderen bens så skikkelse, konen den for
        af han vi, de om. Kraftigt timer den herskab fugle den blev, fader
        skulle.</p>
    """,
    u"""
     <p>Vil hang om et, vandet skud den de. Rørene han, vel i styg selv åben de,
        ind brød rundt på få som i. Klappede lad blev du, over klogere. Og
        verden at og hvor der den, vil godt. Og kom han den ænderne døren
        katten, den da af for men, at gik sin fordi sortgrå jer.</p>
    """,
    u"""
     <p>Men dem eget anden i og, nat da, mig lad anden for når da fader. De i,
        ikke i at, til tage, og sammen nød katten af let. På en i gør er, var
        sted meget rundt sådan er. Svaner til så skud tunge tæt ind, hun gamle
        hvor tænkte hane, hele deres pip, en ske kommer, end grønne er billede.
        De de den således var den dyrene. Bidt vil aldrig er, tykningen høne
        blev bliver de som hvor, bange sprang der over den gamle, ælling i fra
        stakkels nu. Moder lå de and ja dejlighed, ville kender og ikke i. Alt
        lige, styg hvad i og kunne får. Sagde passer fjer bare lå to.</p>
    """,
    u"""
     <p>Ravnen han sammen, nogen stuen, smutte mig som ællingen, godt vidste små
        at de ålehoved dejlige. Lykkedes er andrik hanner ud så natten, rundt
        det hals med og men, øjnene hans da, af aldrig. Længe herskab og de,
        hang jeg sagde det den, bidt derved i, andre ællingemoderen, tungen hun
        og ællinger sig med søer. I vil andre, samme nogle der dejlige og fløj,
        klare børn kom, solen styg set. Om den, humør om viste ud lille ja lov,
        i og men aften. Den velsignede som alle var til men, nær den små eller i
        ud fangst.</p>
    """,
    u"""
     <p>Katten tunge. Og høje thi og kalkunæg svaner det, er midt hvor spinde
        trægrenene verden blevet, sig hen men vil, kongelige dem sådan til er
        der, i de af i om havde her. æde vandet den, de høje den køn den har,
        rede og side æbletræerne, man det, en deres ganske og gik. Syrenerne op
        ælling, sin var forunderlig ikke rappe, om luften kom hun, set derfor
        dukkede, snart den de så det. Kastet mig, halsen du så igen den men jer,
        dig de åben lær varmt jeg gamle, alligevel følte. Ville kunne vandet og
        og så blev, både det hvide har den lide et, holde om for lov derinde rød
        ællingen, og der lige hovedet jeg, og jo moderen.</p>
    """,
    u"""
     <p>Jeg ud vandet deres kunne, sætter i sætte, den din eller, var hende
        hønen rette for. Spurgte men de vingen, styg af og ikke sig født en,
        ingen plask, lukkede nej ville familier så være, når gik mener lide at
        End kun til pip side ællingen de, samme at en så, han æggeblommerne,
        ham og ben ville for der men, skulle så rappe prøve sivene hun strakte.
        Til er i har solskinnet, hinanden se, ikke jer de, ikke så den. Den
        hjertet ventede værre han, på troede vil lige sande, folk han når, det
        hinanden have at råbte men det, den så og lidt hun hun hvide. Jer det.
        ællingen støj og har thi en og, stor da at gode ikke ikke havde. Lærer
        alle sig konen, når og og, en have om og.</p>
    """,
    u"""
     <p>Vil velsignet lidt ham se nakken, stakke gør lød lidt, de måtte og agt
        sin den, den dem værre som så i morgnen. Betaget langt lykke og i og,
        han sådan over sad mellem svømme eget. De andre, dejligt have længe agt
        af de, på ingen. Er ikke og, blev med, så imod, muren skrig af jeg han.
        Af svaner bøjede stakkel til den, har så lad pip, fordi den. Ind mig og
        de, hænderne vel dem, sted uger hen og, på ham af kunne. I rap nu holder
        knagede over, skød styg så ja så over, de rigtig nye aldrig så, nu men
        hele kalkun den efteråret. Stak sig nu dyr i, benene rejste spot, ganske
        grønne andrik den misundte skoven, af flyve, der på den så så dejligste
        dem. Bedrøveligt ællinger så han ikke med det, sne det, derpå lad den
        tage havren og dejlighed, stærkere det. Den sig forstår i enge, sagde
        kommet og and tre. Dræbes morgnen holdt at er midt han, største derinde
        jer, vidt dig bøjede flyde. Værre skreg, alligevel og et sparkes på, til
        det og den måtte bens blev.</p>
    """,
    u"""
     <p>Hun personen og nej hen meget, desuden det, lange hvem sin næbbet lå at
        gang, hele går lå kommet på. Brug midt om godt, også katten, måtte
        nappes den. Vejr så i moder, store ælling så så nu ud klukke, så op
        have, i nykker lade søer i. Af hen ud. Kan disse i. Stod sted de været
        den måtte ægget, det så, af længere midt velsignede så den tænder, dage
        så lykkelige vingen ligesom fik let. De du på, den det nå sagde på og i,
        ham når andre engang ville. Vil og flere så den, de vandfladen altid,
        den om på ned.</p>
    """,
    u"""
     <p>Lagde stakke forunderlig luften, grimhed se. Ganske og ind den side om,
        hun eller den, er for. Ben vi varmt sagde du fy fæle. Den den strøg den.
        Verden tag ællingen røde rundt og falde, kan nu alle hang. Derfor dem
        med sin der, tre faldt. Skikkelse selv lo, faldt så over den og den for.
        Straks fortræd men, det sagde kan, bare skræppeblade ud forstå, alle
        bruste. Kendte og smutte den and du, at børn sagde nej den, og min, og
        dig dybe godt ventede tykkeste. Få derinde i når længere, at dog
        kræfter, der så, sagde eng bide rigtignok. Han bruste havde ikke
        trægrenene personen, dog han sammen end.</p>
    """,
    u"""
     <p>Skal stærkere, kunne jeg. Mig dem solen en, sivene de ungen det og ikke
        op, ud på alt, ham og på. Andre og, fugle lidt er aldrig, mose og, av så
        så hønen ikke børnene. Kom hvor måtte var. Hævede tag få den varm det
        herved. En så og bøjede, ikke de, til den at fortræd men man højt. Født
        i, eller den det, på slikkede stod vingerne slog, godt jeg det men, hun
        måtte den. Til tør, på en nu at, på men hun falde syrenerne en.</p>
    """,
    u"""
     <p>Går er det de jeg lægger rigtig, hun pustede han fik og andegården et,
        puffet rent stykker var, op det var en store, lige sivene hjerte det og
        dig det. Rap slog mig ikke han, rap langt lykkelig egne ikke eller sine,
        tider ind med. Har en hele gik ja disse foden, vide en anden. Han
        varmere se kommer flere ikke, dig ser, i hang ligner i spind have. I ham
        visit den, strakte var løb grimme man dage til, sted herskab og imod med
        har, knagede han fløj hvad unge tak ælling. Rettere vandet var, havde du
        midt en gnistrede, havren i sit han sagde thi lige. Skreg vandet, ham i
        dyr. Styg i at ikke, drejede så så eller over de klogere, grenene rap
        ælling æg den han, som nogle den, af han. Og de og ælling blev kunne, at
        råbte onde for der dem, det de så det lukkede og. Være der så begyndte
        nej ud i, truget sagde er aldrig, de der se rejste i egne på, på været
        om og ingen siv samme, den og med få. Det den den kom alle ællingen, i
        tænder dejligt at men vingerne, den af vinteren al ikke, forunderlig
        rundt buskene er få have kan.</p>
    """,
    u"""
     <p>Kan moderen det lykke om mod, hovedet og så fik, fæl i ingen de tre hver
        blev. Var uden bag vil da alle ben, igen blev og fordi, i sagde klask
        konen sagde og, megen det at det. Er du havde lov nåede godt at, den er
        den tåle, vildænderne få havren at. Egne for det, ved de høet hen det
        mund, brød der men alle i at, æg mod skal eller, noget af. De kan
        hovedet, nu der med set det mindste, samme and igen ovenover op, efter
        prægtige det sidst sin, skrækkelig var skreg visit. De holdt gode den ud
        og. Mosevand fløj havren ikke, den megen ondt oh er og, der sig mig nar
        det ikke han. Den over ikke så, hårdt skal unge sivene det blev, om
        skab, ud fløj. Kommer nærme se, i de al vil de skud, i sagde på på det
        ælling, og at dig, ællingen i er kold lå mindste.</p>
    """,
    u"""
     <p>Tage billede, har sætte vandet. Længere fra var og sig efter, om den,
        før den så det de, med snart jeg, den den. Elendigt moder den og sig,
        vil fordi en fugl kraftigt, den og ganske vand fryse den. Og du jeg til
        rigtignok hvor ganske. Den turde hang tre, kom skreg en det, har i, til
        er, dejligt gifter i stykker kan. Sagde ind så hold, skarer den ting og
        det. Og i har at, sig for og, skyer med op fordi et det du, dyrene tålt
        misundte bare. Har i at katten, verden så sagde, anden er. Hovedet for
        endnu samme som den, ud har, en æg at, lægge ænderne til bedre. Om
        stakkels, over og den lyst var da for, ikke ind, lige efter, op
        ællingemoderen og give længe ællingen. Nå ned sagde, det se den, sad
        krogen drømte lære, falde et for hjemme, til rap.</p>
    """,
    u"""
     <p>Om var han den falde, jeg i sig skulle ene gnistre. Huset de jeg fæl ud
        fordi hen, af ingen ja familie oh storken. Så i vandet, altid du varmt
        havde imod ganske æggeblommerne, selv anden tænkte øjnene stor til, og
        åbne, ikke rar da. For oprejste stak af aldrig lange sagde, af på, ikke
        fór over jaget sagde vandet, alle ked ned gå af du varmt. Vildænderne
        eget kornet ude sagde, rejste ikke ikke de, på set lad men børn. At af
        skreg. Fattigt bunden snablen, tænkte set med af. Og oprejste så,
        begyndte ham hunden lagde og, ad se på siden rød. Hinanden dejlige rar
        stille og, du og en op og han, fuglene så lykke nød vildgasserne ved i,
        sagde du anden den det og ikke, skinnede store hjerte at barn af.</p>
    """,
    u"""
     <p>Om så sagde, så løb. Hjertet det, til kold små på under vandet, kan
        ænderne vandet, stor nåede sortgrå kold. Ved at stor, æg fløj elendigt
        blevet og lige løb, hjemme vingen de, spurgte lide men imellem. Gnistre
        og her på der sang, man lå dejligt kejser mig visit mose, al have
        hovedet, at han at var, et vinter en ned tre tungen. Været der, dem
        prøve, vildgæs og ikke børn, dejlighed og prøvet i bruge de, børnene
        han. Blev blev, så blevet, der har sagde svømme ikke stuen, verden
        dejligt så, med sønnike dukkede ægget for. Af ud sig ville trækfugl,
        om konen det før, sit ud ja nyfaldne ganske over sjælden, måtte
        forunderlig største på for og lægge.</p>
    """,
    u"""
     <p>Hovedet de huggede for længe hun, og hen ja. Tænkte lange bruge den i
        spinde din, vejr pigen visit hårene alle gør, kraftigt andre han og
        ravnen blevet. Sin var. End at i dig kan, den smidige så hun at det,
        hvad for ned katten, sig ingen på der, med mig på undselig på om troede.
        En hun nå familie en skal, i må ud, den give i gider ællingen. Det så
        kan ser, lad er ikke sig de sig, ællingemoderen den så æg og, eng igen
        solen vil. Sloges at i grimme, det sig, skarer dem ikke endnu, muren
        blæst ham hænderne og dem, and det sit elendigt. Det på var, aparte hun
        grene den god det ham, godt han var små, for noget, der blod de der. Pip
        det sidst går og ællingen, den af vidste flød lært bar de, alle stod
        jeg. Slog på alle, man gammel af med gået var, dog vil benene bliver,
        kom fugle ællingen som, ligget ællingemoderen og sætter.</p>
    """
    ,u""
    ]
    
    from random import randint, sample
    
    def generate_section_content():
        return "".join(sample(random_paragraphs, randint(1,3)))
    c.execute("select id from documentation")
    while True:
        insertcursor = connection.cursor()
        row = c.fetchone()
        if row == None:
            break
        (id,) = row
        for x in xrange(randint(3,9)):
            order = x
            title = "Unavngivet sektion %d" % x
            content = generate_section_content()
            insertcursor.execute("""
                insert into documentation_section(`title`, `content`, `order`, `documentation_id`, `deleted`)
                values(%s, %s, %s, %s, false)
            """, (title, content, order, id))
        insertcursor.close()
    connection.commit()
    c.close()
    
if __name__ == "__main__":
    connection = get_connection()
    generate_institutions(connection)
    generate_users(connection)
    generate_documents(connection)
    generate_document_sections(connection)
    connection.close()
