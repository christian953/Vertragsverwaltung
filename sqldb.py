from sqlobject import *
import encrypt_decrypt

sqlhub.processConnection = connectionForURI('sqlite:Vertragswarner.db')

colnames = [
    "kategorie", "bezeichnung", "start_datum", "enddatum", "kuendigungsdatum", "webseite", "nutzername", "passwort"
]


# Kategorie, Bezeichnung, Start-, End- und spätestem Kündigungsdatum, Webseite, Nutzername und Passwort.
class Vertragswarner(SQLObject):
    kategorie = StringCol()
    bezeichnung = StringCol()
    start_datum = DateCol()
    enddatum = DateCol()
    kuendigungsdatum = DateCol()
    webseite = StringCol()
    nutzername = StringCol()
    passwort = StringCol()
    iv = StringCol()


Vertragswarner(kategorie="b", bezeichnung="b", start_datum="2002-10-10", enddatum="2002-10-10",
               kuendigungsdatum="2002-10-10",
               webseite="a", nutzername="a", passwort="c", iv="d")

Vertragswarner.createTable(ifNotExists=True)


def getValues(orderBy):
    values = Vertragswarner.select(orderBy=colnames[orderBy])
    rows = []
    values = list(values)[:8]
    for row in range(0, 8 if len(values) > 8 else len(values)):
        cells = []
        cells.append(values[row].kategorie)
        cells.append(values[row].bezeichnung)
        cells.append(values[row].start_datum.strftime("%Y-%m-%d"))
        cells.append(values[row].enddatum.strftime("%Y-%m-%d"))
        cells.append(values[row].kuendigungsdatum.strftime("%Y-%m-%d"))
        cells.append(values[row].webseite)
        cells.append(values[row].nutzername)
        cells.append(values[row].passwort)
        cells.append(values[row].id)
        rows.append(cells)
    return rows


def update(id, values):
    vetrag = Vertragswarner.get(id)
    vetrag.kategorie = values[0]
    vetrag.bezeichnung = values[1]
    vetrag.start_datum = values[2]
    vetrag.enddatum = values[3]
    vetrag.kuendigungsdatum = values[4]
    vetrag.webseite = values[5]
    vetrag.nutzername = values[6]
    vetrag.passwort = values[7]


def remove(_id):
    print(_id)
    Vertragswarner.delete(_id)


def add(values):
    passwort = encrypt_decrypt.encrypt(values[6])
    Vertragswarner(kategorie=values[0], bezeichnung=values[1], start_datum=values[2], enddatum=values[3],
                   kuendigungsdatum=values[3],
                   webseite=values[4], nutzername=values[5], passwort=passwort[0], iv=passwort[1])
