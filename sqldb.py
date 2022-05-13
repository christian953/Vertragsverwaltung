from sqlobject import *
import encrypt_decrypt
import datetime

sqlhub.processConnection = connectionForURI('sqlite:Vertragswarner.db')

colnames = [
    "kategorie", "bezeichnung", "start_datum", "enddatum", "kuendigungsdatum", "webseite", "nutzername", "passwort"
]  # List of internal colnames of database used for sorting


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


class Masterpassword(SQLObject):
    password = BLOBCol()
    iv = BLOBCol()


def setDefaulPassword():
    password = encrypt_decrypt.encrypt("123")
    Masterpassword(password=password[0], iv=password[0])


Vertragswarner.createTable(ifNotExists=True)
Masterpassword.createTable(ifNotExists=True)
if len(list(Masterpassword.select())) == 0:
    setDefaulPassword()


def getValues(orderBy):
    """Returns first 8 resuslts of database as list of lists. Christian"""
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
    """Updates row in database to passed values. Christian"""
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
    """Deletes row in database by ID. Christian"""
    print(_id)
    Vertragswarner.delete(_id)


def add(values):
    """Adds a new row to the Database. Christian"""
    passwort = encrypt_decrypt.encrypt(values[6])
    print(values)
    Vertragswarner(kategorie=values[0], bezeichnung=values[1], start_datum=values[2], enddatum=values[3],
                   kuendigungsdatum=values[4],
                   webseite=values[5], nutzername=values[6], passwort=str(passwort[0]), iv=str(passwort[1]))


def updatePassword(password):
    password = encrypt_decrypt.encrypt(password)
    pwdb = Masterpassword.get(1)
    pwdb.password = password[0]
    pwdb.iv = password[1]


def getPassword():
    password = Masterpassword.get(1)
    password = encrypt_decrypt.decrypt(bytes(password.password), password.iv)
    return password
